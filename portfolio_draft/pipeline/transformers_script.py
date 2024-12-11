import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder

class FeatureFiller(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._col_names = None
        self._col_dict = None
        
    def fit(self, X, y=None):
        self._col_names = list(X.columns)
        
        init_dict = X.dtypes.apply(lambda x: x.name).to_dict()
        self._col_dict = {}
        for col, dtype in init_dict.items():
            self._col_dict.setdefault(dtype, []).append(col)      
        return self

    def transform(self, X, y=None):
        # print('Running FeatureFiller')
        new_X = pd.DataFrame(columns=self._col_names)

        for col_type in self._col_dict:
            columns = self._col_dict[col_type]
            new_X[columns] = new_X[columns].astype(col_type)
        
        new_df = pd.concat([new_X, X])
        # print("Finished FeatureFiller")
        return new_df

    def get_feature_names(self):
        return self._col_names

    def get_feature_names_out(self):
        return self._col_names

class TrueFalseTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._col_names = None

    def fit(self, X, y=None):
        self._col_names = list(X.columns)
        return self

    def transform(self, X, y=None):
        # print('Running TrueFalseTransformer')
        X = X.replace({'None':np.nan}).fillna('-1')
        X = X.replace({'true':'1', 'false':'0'})
        X = X.apply(pd.to_numeric, args=('coerce',))
        # print("Finished TrueFalseTransformer")
        return X

    def get_feature_names(self):
        return self._col_names

    def get_feature_names_out(self):
        return self._col_names

class DateTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._col_names = None

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        # print('Running DateTransformer')
        X = X.replace({'None':np.nan})
        temp_df = pd.DataFrame(index=X.index.copy())

        for col in X.columns:
            X[col] = pd.to_datetime(X[col])
            temp_df[f'{col}-month'] = X[col].dt.month.astype(float)
            temp_df[f'{col}-day_of_week'] = X[col].dt.dayofweek.astype(float)
            temp_df[f'{col}-hour'] = X[col].dt.hour.astype(float)
            temp_df[f'{col}-day_of_month'] = X[col].dt.day.astype(float)
            temp_df[f'{col}-is_month_start'] = X[col].dt.is_month_start.astype(int)
            temp_df[f'{col}-is_month_end'] = X[col].dt.is_month_end.astype(int)
        self._col_names = list(temp_df.columns)
        temp_df = temp_df.fillna(-1)
        # print("Finished DateTransformer")
        return temp_df

    def get_feature_names(self):
        return self._col_names

    def get_feature_names_out(self):
        return self._col_names

class FloatTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._col_names = None

    def fit(self, X, y=None):
        self._col_names = list(X.columns)
        return self

    def transform(self, X, y=None):
        # print('Running FloatTransformer')
        X = X.replace({'None':np.nan})
        for col in self._col_names:
            if X[col].dtype != 'float':
                X[col] = X[col].astype(float)
        X = X.fillna(-1.0)
        # print("Finished FloatTransformer")
        return X

    def get_feature_names(self):
        return self._col_names

    def get_feature_names_out(self):
        return self._col_names

class ListMaxTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._col_names = None

    def fit(self, X, y=None):
        self._col_names = list(X.columns)
        return self

    def transform(self, X, y=None):
        # print('Running ListMaxTransformer')
        X = X.replace({'None':np.nan})
        temp_df = pd.DataFrame(index=X.index.copy())
        for col in self._col_names:
            if X[col].dtype == 'str':
                X[col].fillna('-1', inplace=True)
                X[col] = X[col].str.split(pat=',').apply(set).apply(list)
            temp_series = X[col].explode()
            temp_series = temp_series.replace({'true':'1', 'false':'0'}).fillna('-1').apply(pd.to_numeric, args=('coerce',))
            temp_series = temp_series.groupby(temp_series.index).max()
            temp_df = temp_df.merge(temp_series, left_index=True, right_index=True, how='outer')
        temp_df = temp_df.fillna(0)
        # print("Finished ListMaxTransformer")
        return temp_df

    def get_feature_names(self):
        return self._col_names

    def get_feature_names_out(self):
        return self._col_names

class ListNuniqueTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._col_names = None

    def fit(self, X, y=None):
        self._col_names = list(X.columns)
        return self

    def transform(self, X, y=None):
        # print('Running ListNuniqueTransformer')
        X = X.replace({'None':np.nan})
        temp_df = pd.DataFrame(index=X.index.copy())
        for col in self._col_names:
            if X[col].dtype == 'str':
                X[col] = X[col].dropna().str.split(pat=',').apply(set).apply(list)
            temp_series = X[col].explode()
            temp_series = temp_series.groupby(temp_series.index).nunique()
            temp_df = temp_df.merge(temp_series, left_index=True, right_index=True, how='outer')
        temp_df = temp_df.fillna(0)
        # print("Finished ListNuniqueTransformer")
        return temp_df

    def get_feature_names(self):
        return self._col_names

    def get_feature_names_out(self):
        return self._col_names

class DescStatTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._col_names = None

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        # print('Running DescStatTransformer')
        X = X.replace({'None':np.nan})
        temp_df = pd.DataFrame(index=X.index.copy())
        for col in X.columns:
            if X[col].dtype == 'str':
                X[col].fillna('-1', inplace=True)
                X[col] = X[col].str.split(pat=',').apply(set).apply(list)
            temp_series = X[col].explode()
            temp_series = temp_series.fillna('-1').apply(pd.to_numeric, args=('coerce',))
            temp_series = temp_series.groupby(temp_series.index).agg(['min', 'max', 'mean', 'std', 'nunique'])
            temp_series.columns = [f'{col}-{x}' for x in temp_series.columns]
            temp_df = temp_df.merge(temp_series, left_index=True, right_index=True, how='outer')
        temp_df = temp_df.fillna(0)
        self._col_names = list(temp_df.columns)
        # print("Finished DescStatTransformer")
        return temp_df

    def get_feature_names(self):
        return self._col_names

    def get_feature_names_out(self):
        return self._col_names

class OneHotTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._filler = 'ml_empty'
        self._col_names = None
        self._encoder = None
        self._transformer = None
        self._transformed_feats = []

    def fit(self, X, y=None):
        self._col_names = X.dropna(axis=1, how='all').columns
        X = X[self._col_names].fillna(self._filler)
        self._encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        self._transformer = self._encoder.fit(X)
        self._transformed_feats = self._transformer.get_feature_names_out()
        return self

    def transform(self, X, y=None):
        # print('Running OneHotTransformer')
        X = X.replace({'None':np.nan}).fillna(self._filler)
        X = self._transformer.transform(X[self._col_names])
        # print("Finished OneHotTransformer")
        return X

    def get_feature_names(self):
        return list(self._transformed_feats)

    def get_feature_names_out(self):
        return list(self._transformed_feats)

class MultilabelTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._filler = 'ml_empty'
        self._encoder = None
        self._col_names = None

    def fit(self, X, y=None):
        X = X.fillna(self._filler).str.split(pat=',').apply(set).apply(list)
        self._encoder = MultiLabelBinarizer()
        self._encoder.fit(X)
        self._col_names = [X.name + '_' + x for x in self._encoder.classes_]
        return self

    def transform(self, X, y=None):
        # print('Running MultilabelTransformer')
        X = X.replace({'None':np.nan})
        X = X.fillna(self._filler).str.split(pat=',').apply(set).apply(list)
        trans_array = self._encoder.transform(X)
        df = pd.DataFrame(trans_array, columns=self._col_names, index=X.index)   
        # print("Finished MultilabelTransformer")     
        return df

    def get_feature_names(self):
        return self._col_names

    def get_feature_names_out(self):
        return self._col_names
    
class DropSingleValueCols(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._col_index = []
        self._col_names = []
        
    def fit(self, X, y=None):
        if type(X) == np.ndarray:
            # print('Processing numpy array')
            X = pd.DataFrame(X)
        # elif type(X) == pd.core.frame.DataFrame:
        #     print('Processing pandas dataframe')
        for i in range(len(X.columns)):
            if X.iloc[:,i].nunique() > 1:
                self._col_index.append(i)
        self._col_names = list(X.iloc[:,self._col_index].columns)
        return self
    
    def transform(self, X, y=None):
        # print('Running DropSingleValueCols')
        if type(X) == np.ndarray:
            print('Processing numpy array')
            X = pd.DataFrame(X)
        # elif type(X) == pd.core.frame.DataFrame:
        #     print('Processing pandas dataframe')
        X = X[self._col_names]
        # X = X.iloc[:,self._col_index]
        # print("Finished DropSingleValueCols")
        return X
    
    def get_feature_names(self):
        return self._col_names

    def get_feature_names_out(self):
        return self._col_names
       
class RemoveCollinearity(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._corr_dict = {}
        self._drop_cols = set()
        self._col_index = []
        self._col_names = []
        
    def fit(self, X, y=None):
        drop_list = []
        if type(X) == np.ndarray:
            # print('Processing numpy array')
            X = pd.DataFrame(X)
        # elif type(X) == pd.core.frame.DataFrame:
        #     print('Processing pandas dataframe')
        corr_df = X.corr()
        for i, col in enumerate(corr_df.columns):
            sliced_col = abs(corr_df.iloc[i+1:, i])
            corr_feats = sliced_col[sliced_col > .97].index.tolist()
            if len(corr_feats) > 0:
                self._corr_dict[col] = corr_feats
                drop_list += corr_feats
        self._drop_cols = set(drop_list)
        # print('Collinear feature drop list:', drop_list)
        print('Number of collinear feature:', len(drop_list))
        self._col_names = list(set(X.columns) - self._drop_cols)
        for i, col in enumerate(X.columns):
            if col in self._col_names:
                self._col_index.append(i)
        return self
    
    def transform(self, X, y=None):
        # print('Running RemoveCollinearity')
        if type(X) == np.ndarray:
            # print('Processing numpy array')
            X = pd.DataFrame(X)
        # elif type(X) == pd.core.frame.DataFrame:
        #     print('Processing pandas dataframe')
        X =  X[self._col_names]
        # X =  X.iloc[:,self._col_index]
        # print("Finished RemoveCollinearity")
        return X
    
    def get_feature_names(self):
        return self._col_names

    def get_feature_names_out(self):
        return self._col_names
    
class SetColumnOrder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._col_names = []
        
    def fit(self, X, y=None):
        if type(X) == np.ndarray:
            # print('Processing numpy array')
            X = pd.DataFrame(X)
        # elif type(X) == pd.core.frame.DataFrame:
        #     print('Processing pandas dataframe')
        self._col_names = list(set(X.columns))
        return self
    
    def transform(self, X, y=None):
        # print('Running SetColumnOrder')
        if type(X) == np.ndarray:
            # print('Processing numpy array')
            X = pd.DataFrame(X)
        # elif type(X) == pd.core.frame.DataFrame:
        #     print('Processing pandas dataframe')
        X =  X[self._col_names]
        # X =  X.iloc[:,self._col_index]
        # print("Finished SetColumnOrder")
        return X
    
    def get_feature_names(self):
        return self._col_names

    def get_feature_names_out(self):
        return self._col_names
