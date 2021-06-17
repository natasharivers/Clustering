########################### NULLS BY COLUMN ###########################

#get nulls by column
def nulls_by_col(df):
    num_missing = df.isnull().sum()
    rows = df.shape[0]
    prcnt_miss = num_missing / rows * 100
    cols_missing = pd.DataFrame({'num_rows_missing': num_missing, 'percent_rows_missing': prcnt_miss})
    return cols_missing

########################### NULLS BY ROW ###########################

#get nulls by row
def nulls_by_row(df):
    num_missing = df.isnull().sum(axis=1)
    prcnt_miss = num_missing / df.shape[1] * 100
    rows_missing = pd.DataFrame({'num_cols_missing': num_missing, 'percent_cols_missing': prcnt_miss})\
    .reset_index()\
    .groupby(['num_cols_missing', 'percent_cols_missing']).count()\
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
    num_cols = [cols for col in df.columns if df[col].dtype != '0']
    cat_cols = [col for col in df.columns if col not in num_cols]
    
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
