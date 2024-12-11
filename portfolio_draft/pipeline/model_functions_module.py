import numpy as np
import pandas as pd
import importlib
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn import set_config
from sklearn.model_selection import RandomizedSearchCV, cross_validate
import skexplain
import shap
import alibi
from transformers_script import FeatureFiller
from transformers_script import DropSingleValueCols
from transformers_script import RemoveCollinearity
from transformers_script import SetColumnOrder
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.metrics import precision_score, roc_auc_score, f1_score

def define_algo_pipe(algo, col_dict):
    transformer_list = []
    tModule = importlib.import_module("transformers_script")
    key_list = [x for x in col_dict.keys() if not x == 'drop_cols']
    for key in key_list:
        trans_function = getattr(tModule, col_dict[key]['transformer'])
        if key == 'list_to_labels':
            for col in col_dict[key]['columns']:
                step_name = key + '_' + col
                transformer_list.append((step_name, trans_function(), col))
        else:
            transformer_list.append((key, trans_function(), col_dict[key]['columns']))
    transformer_list.append(("drop_cols", 'drop', col_dict["drop_cols"]["columns"]))
    preprocessor = ColumnTransformer(transformer_list)
    
    all_preprocess = Pipeline([
        ('featurefiller', FeatureFiller()),
        ('preprocess', preprocessor),
        ('dropsingle', DropSingleValueCols()),
        ('removemulticollinear', RemoveCollinearity()),
        ('setcolumorder', SetColumnOrder())])

    algo_pipe = Pipeline([
        ('all_preprocess', all_preprocess),
        ('algorithm', algo)])
    return algo_pipe

def train_model(algo, algo_data, col_dict, Xtrain, ytrain):
    metric_result_dict = {}
    results = None
    print(algo_data['class'])
    try:
        if 'defaults' in algo_data:
            model = algo(**algo_data['defaults'])
        else:
            model = algo()
        model_pipe = define_algo_pipe(model, col_dict)
        results = cross_validate(model_pipe, Xtrain, ytrain, cv=5, scoring=['accuracy', 'precision', 'f1', 'recall', 'roc_auc'])
        for result in results.keys():
            results[result] = results[result].tolist()
        metric_result_dict[algo_data['class']] = results
    except Exception as error:
        print("Error on", algo_data['class'])
        print("Error:", error)
    print('\n')
    print(algo_data['class'], "Result Dictionary:")
    print(results)
    return metric_result_dict

def compile_algo_metrics(metric_dict):
    metric_result_df = pd.DataFrame(metric_dict).T
    metric_desc_stat_df = pd.DataFrame()
    for col in metric_result_df.columns:
        if 'time' in col:
            continue
        else:
            mean_col = col + '_mean'
            stdv_col = col + '_stdev'
            penalized = col + '_penalized'
            metric_desc_stat_df[mean_col] = metric_result_df[col].apply(np.mean)
            metric_desc_stat_df[stdv_col] = metric_result_df[col].apply(np.std)
            metric_desc_stat_df[penalized] = metric_desc_stat_df[mean_col] * (1 - metric_desc_stat_df[stdv_col])
    metric_desc_stat_df = metric_desc_stat_df.sort_values([
        'test_f1_penalized',
        'test_roc_auc_penalized',
        'test_recall_penalized',
        'test_precision_penalized',
        'test_accuracy_penalized'], ascending=False)
    return metric_desc_stat_df

def tune_best_algo(algo, algo_data, col_dict, Xtrain, ytrain):
    algo_pipe = define_algo_pipe(algo(), col_dict)
    param_grid = dict(('algorithm__'+key, value) for (key, value) in algo_data['params'].items())
    search_params = {"estimator": algo_pipe,
                     "cv": 5,
                     "param_distributions": param_grid,
                     "scoring": {'f1':'f1',
                                 'auc':'roc_auc'},
                     "verbose": 5,
                     "refit": "f1",
                     "random_state": 12}
    print("Tuning for hyperparameters")
    tuner = RandomizedSearchCV(**search_params)
    print("Training model")
    tuner.fit(Xtrain, ytrain)
    model = tuner.best_estimator_
    print(model)
    return model

def metrics_row(y_test, model, testX):
    predictions = model.predict(testX)
    proba_predictions = model.predict_proba(testX)[:, 1]
    
    accuracy = accuracy_score(y_test, predictions)
    conf_matrix = confusion_matrix(y_test, predictions)
    precision = precision_score(y_test, predictions)
    roc_auc = roc_auc_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    
    conf_matrix_norm = np.round(conf_matrix / conf_matrix.sum(axis=1), 3)
    
    annotation_list = []
    lbls = ['True Negative', 'False Positive', 'False Negative', 'True Positive']
    ct = 0
    for i in range(conf_matrix.shape[0]):
        tmp = []
        for x in range(conf_matrix[i].shape[0]):
            val = f"{lbls[ct]}\n\nCount: {conf_matrix[i][x]}\nActl Rate: {conf_matrix_norm[i][x]}"
            tmp.append(val)
            ct += 1
        annotation_list.append(tmp)
        
    result_dict = {"Accuracy": round(accuracy, 3),
                   "Precision": round(precision, 3),
                   "F1": round(f1, 3),
                   "Recall": round(recall, 3),
                   "ROC AUC": round(roc_auc, 3),
                   "conf_matrix": annotation_list}
    return result_dict

def explainability_mods(model, Xtrain):
    preprocess_pipe = model.named_steps['all_preprocess']
    train_processed = preprocess_pipe.transform(Xtrain)
    just_model = model.named_steps['algorithm']
    
    shap_mask = shap.maskers.Partition(train_processed,
                                       max_samples=1000)
    shap_explainer = shap.Explainer(just_model.predict,
                                    shap_mask,
                                    algorithm = "permutation")
    
    predict_fn = lambda x: just_model.predict(x)
    anchor_explainer = alibi.explainers.AnchorTabular(predict_fn, train_processed.columns, seed=1)
    anchor_explainer.fit(train_processed.to_numpy())
    
    return shap_explainer, anchor_explainer
