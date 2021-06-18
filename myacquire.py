
#import libraries
import pandas as pd
import numpy as np
import os
from pydataset import data

# acquire
from env import host, user, password


################################### GET CONNECTION FUNCTION ###################################
def get_connection(db_name):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


################################### GET ZILLOW FUNCTION ###################################
def get_zillow():
    '''
    This function reads in the Zillow data from the Codeup db
    with properties_2017, predictions_2017 and propertylandusetype tables joined
    returns: a pandas DataFrame 
    '''
    
    zp_query = '''
    SELECT *
    FROM predictions_2017
    LEFT JOIN properties_2017 ON predictions_2017.parcelid = properties_2017.parcelid
    LEFT JOIN airconditioningtype ON properties_2017.airconditioningtypeid= airconditioningtype.airconditioningtypeid
    LEFT JOIN architecturalstyletype ON properties_2017.architecturalstyletypeid= architecturalstyletype.architecturalstyletypeid
    LEFT JOIN buildingclasstype ON properties_2017.buildingclasstypeid= buildingclasstype.buildingclasstypeid
    LEFT JOIN heatingorsystemtype ON properties_2017.heatingorsystemtypeid= heatingorsystemtype.heatingorsystemtypeid
    LEFT JOIN propertylandusetype ON properties_2017.propertylandusetypeid= propertylandusetype.propertylandusetypeid
    LEFT JOIN storytype ON properties_2017.storytypeid= storytype.storytypeid
    LEFT JOIN typeconstructiontype ON properties_2017.typeconstructiontypeid= typeconstructiontype.typeconstructiontypeid
    where properties_2017.latitude is not null and properties_2017.longitude is not null
    '''
    return pd.read_sql(zp_query, get_connection('zillow'))

################################### GET ZILLOW CSV FUNCTION ###################################

def get_zillow_file():
    if os.path.isfile('zillow.csv'):
        df = pd.read_csv('zillow.csv', index_col=0)
    
    else:
        df = get_zillow()
        df.to_csv('zillow.csv')
    
    return df
