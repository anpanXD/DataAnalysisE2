import pandas as pd
import numpy as np

# read data file

def parse_file(x):
    df0 = pd.read_csv(x)
    
    # extract relevant columns
    
    df = df0[  
    ['Race_ethnicity', 'Age_group', 'Topic', 'Denominator', 'Year', 'Zip_code', 'Primary_Neighborhood', 'Death_tooltip', 'Number_with_outcome']  ]
    
    pd.set_option('mode.chained_assignment', None)
    df['Number_with_outcome'] = df['Number_with_outcome'].replace({',':''}, regex = True).astype(float)
    df['Denominator'] = df['Denominator'].replace({',':''}, regex = True).astype(float)
    df['Topic'] = df['Topic'].astype(str)
    df['Race_ethnicity'] = df['Race_ethnicity'].astype(str)
    
    topics_to_drop = df[df['Topic'] == 'CAUSE OF DEATH'].index
    df.drop(topics_to_drop, inplace = True)
    
    # rename
    
    df = df.rename( columns={'Race_ethnicity':'race_ethnicity', 'Age_group':'agegroup', 'Denominator':'denominator',
                            'Year':'year', 'Zip_code':'zipcode', 'Primary_Neighborhood':'primaryneighborhood',
                            'Death_tooltip':'deathtooltip', 'Number_with_outcome':'number_with_outcome', 'Topic':'topic'} )

    return df