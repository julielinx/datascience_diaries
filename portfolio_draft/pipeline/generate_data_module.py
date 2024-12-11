import random
import datetime
import numpy as np
def calc_wts(col, predictability):
    low_wt = 1 - predictability
    col_len = len(col)
    if predictability > 0:
        wts = [predictability] + [(low_wt/(col_len-1)) for x in range(col_len-1)]
    elif predictability == 0:
        wts = [(low_wt/(col_len)) for x in range(col_len)]
    else:
        print('''High weight must be between 0 or greater and less than 1.
              A value of 0 gives equal weight to all values
              A value greater than 0 and less than one gives that weight to the first value and equal weights to all other values''')
    xwts = list(reversed(wts))
    return wts, xwts

def generate_dates(df, target_name, year=2022):
    true_vals = []
    false_vals = []
    month_wts, month_xwts = calc_wts(range(1, 12), 0)
    day_wts, day_xwts = calc_wts(range(1, 31), 0.8)    
    
    t_year = [year for x in range(len(df[df[target_name]==1]))]
    t_month = random.choices(range(1, 12), month_wts, k=len(df[df[target_name]==1]))
    t_day = random.choices(range(1, 31), day_wts, k=len(df[df[target_name]==1]))
    true_collist = zip(t_year,
                       t_month,
                       t_day)
    for yr, mt, dy in true_collist:
        try:
            date = datetime.date(yr, mt, dy)
            true_vals.append(date)
        except ValueError:
            true_vals.append(np.nan)
            
    f_year = [year for x in range(len(df[df[target_name]==0]))]
    f_month = random.choices(range(1, 12), month_xwts, k=len(df[df[target_name]==0]))
    f_day = random.choices(range(1, 31), day_xwts, k=len(df[df[target_name]==0]))
    false_collist = zip(f_year,
                        f_month,
                        f_day)
    for yr, mt, dy in false_collist:
        try:
            date = datetime.date(yr, mt, dy)
            false_vals.append(date)
        except ValueError:
            false_vals.append(np.nan)
    
    return true_vals, false_vals
