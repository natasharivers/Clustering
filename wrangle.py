import pandas as pd

########################### NULLS BY COLUMN ###########################

#get nulls by column
def nulls_by_col(df):
    num_missing = df.isnull().sum()
    rows = df.shape[0]
    prcnt_miss = num_missing / rows * 100
    cols_missing = pd.DataFrame({'num_rows_missing': num_missing, 'pct_rows_missing': prcnt_miss})
    return cols_missing

########################### NULLS BY ROW ###########################

#get nulls by row
def nulls_by_row(df):
    num_missing = df.isnull().sum(axis=1)
    prcnt_miss = num_missing / df.shape[1] * 100
    rows_missing = pd.DataFrame({'num_cols_missing': num_missing, 'pct_cols_missing': prcnt_miss})\
    .reset_index()\
    .groupby(['num_cols_missing', 'pct_cols_missing']).count()\
    .rename(index=str, columns={'index':'num_rows'}).reset_index()
    return rows_missing

########################### SUMMARIZE FUNCTION ###########################
#summarize data in the df
#head, info, describe, value counts, nulls

def summarize(df):
    '''
    this function will take in a single argument (a pandas df) 
    output to console various statistics on said dataframe, including:
    #.head()
    #.info()
    #.describe()
    #.value_counts()
    #observation of nulls in the dataframe
    '''
    #print head
    print('=================================================')
    print('Dataframe head: ')
    print(df.head(3))
    
    #print info
    print('=================================================')
    print('Dataframe info: ')
    print(df.info())
    
    #print descriptive stats
    print('=================================================')
    print('Dataframe Description: ')
    print(df.describe())
    num_cols = [cols for col in df.columns if df[col].dtype != 'O']
    cat_cols = [cols for col in df.columns if col not in num_cols]
    
    #print value counts
    print('=================================================')
    print('Dataframe value counts: ')
    for col in df. columns:
        if col in cat_cols:
            print(df[col].value_counts())
        else:
            print(df[col].value_counts(bins=10, sort = False))
    
    #print nulls by column
    print('=================================================')
    print('nulls in dataframe by column: ')
    print(nulls_by_col(df))
    
    #print nulls by column
    print('=================================================')
    print('nulls in dataframe by row: ')
    print(nulls_by_row(df))
    print('=================================================')

########################### REMOVE COLUMNS FUNCTION ###########################
def remove_columns (df, cols_to_remove):
    df = df.drop(columns = cols_to_remove)
    return df

########################### FILLNA FUNCTION ###########################

def handle_missing_values(df, prop_required_columns = 0.5, prop_required_row=0.75):
    threshold = int(round(prop_required_columns * len(df.index), 0))
    df = df.dropna(axis=1, thresh=threshold)
    threshold = int(round(prop_required_row * len(df.columns), 0))
    df = df.dropna(axis=0, thresh= threshold)
    return df

########################### DATA PREP FUNCTION ###########################

def data_prep(df, cols_to_remove=[], prop_required_columns =0.5, prop_required_row=0.75):
    df = remove_columns(df, cols_to_remove)
    df= handle_missing_values(df, prop_required_columns, prop_required_row)
    return df

########################### UPPER OUTLIER FUNCTION ###########################

#create outlier function
def get_upper_outliers(s, k= 1.5):
    q1, q3 = s.quantile([.25, .75])
    iqr = q3 - q1
    upper_bound = q3 + k * iqr
    return s.apply(lambda x: max([x-upper_bound, 0]))


#apply the function
def add_upper_outlier_columns(df, k=1.5):
    for col in df.select_dtypes('number'):
        df [col + '_outlier_upper'] = get_upper_outliers(df[col], k)
    return df
    
############################## DROP OUTLIERS FUNCTION ##############################


def outlier_bound_calculation(df, variable):
    '''
    calcualtes the lower and upper bound to locate outliers in variables
    '''
    quartile1, quartile3 = np.percentile(df[variable], [25,75])
    IQR_value = quartile3 - quartile1
    lower_bound = quartile1 - (1.5 * IQR_value)
    upper_bound = quartile3 + (1.5 * IQR_value)
    '''
    returns the lowerbound and upperbound values
    '''
    return print(f'For {variable} the lower bound is {lower_bound} and  upper bound is {upper_bound}')