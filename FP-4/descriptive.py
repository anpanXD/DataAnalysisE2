from IPython.display import display,Markdown #,HTML
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import pandas as pd

def parse_csv(x):
    import parse_data as parse
    df = parse.parse_file(x)
    return df

def display_title(s, pref='Figure', num=1, center=False):
    ctag = 'center' if center else 'p'
    s    = f'<{ctag}><span style="font-size: 1.2em;"><b>{pref} {num}</b>: {s}</span></{ctag}>'
    if pref=='Figure':
        s = f'{s}<br><br>'
    else:
        s = f'<br><br>{s}'
    display( Markdown(s) )

# define central and dispersion functions

def central(x, print_output=True):
    x0     = np.mean( x )
    x1     = np.median( x )
    x2     = stats.mode( x ).mode
    return x0, x1, x2


def dispersion(x, print_output=True):
    y0 = np.std( x ) # standard deviation
    y1 = np.min( x )  # minimum
    y2 = np.max( x )  # maximum
    y3 = y2 - y1      # range
    y4 = np.percentile( x, 25 ) # 25th percentile (i.e., lower quartile)
    y5 = np.percentile( x, 75 ) # 75th percentile (i.e., upper quartile)
    y6 = y5 - y4 # inter-quartile range
    return y0,y1,y2,y3,y4,y5,y6

# create central tendency table

def display_central_tendency_table(num=1):
    import parse_data as parse
    df = parse.parse_file('healthassessment.csv')
    df = df.dropna(subset = ['denominator', 'number_with_outcome'])
    display_title('Central tendency summary statistics.', pref='Table', num=num, center=False)
    df_central = ( df[['denominator', 'number_with_outcome']].apply(lambda x: central(x), axis=0) )
    round_dict = {'denominator': 3, 'number_with_outcome': 3}
    df_central = df_central.round( round_dict )
    row_labels = 'mean', 'median', 'mode'
    df_central.index = row_labels
    display( df_central )

# create dispersion table

def display_dispersion_table(num=1):
    import parse_data as parse
    df = parse.parse_file('healthassessment.csv')
    df = df.dropna(subset = ['denominator', 'number_with_outcome'])
    display_title('Dispersion summary statistics.', pref='Table', num=num, center=False)
    round_dict            = {'denominator': 3, 'number_with_outcome': 3}
    df_dispersion         = ( df[['denominator', 'number_with_outcome']] ).apply(lambda x: dispersion(x), axis=0).round( round_dict )
    row_labels_dispersion = 'st.dev.', 'min', 'max', 'range', '25th', '75th', 'IQR'
    df_dispersion.index   = row_labels_dispersion
    display( df_dispersion )

def plots(x):

    import parse_data as parse
    df = parse.parse_file('healthassessment.csv')
    df = df.dropna(subset = ['denominator', 'number_with_outcome'])
    
    df_access = df[['number_with_outcome']].where( df.topic == 'ACCESS TO CARE' )
    df_death = df[['number_with_outcome']].where( df.topic == 'DEATH' )
    df_dental = df[['number_with_outcome']].where( df.topic == 'DENTAL' )
    df_healthcond = df[['number_with_outcome']].where( df.topic == 'HEALTH CONDITION' )
    df_healthbehav = df[['number_with_outcome']].where( df.topic == 'HEALTH BEHAVIOR' )
    df_nutrition = df[['number_with_outcome']].where( df.topic == 'NUTRITION' )
    df_safety = df[['number_with_outcome']].where( df.topic == 'SAFETY' )
    df_socialdeterm = df[['number_with_outcome']].where( df.topic == 'SOCIAL DETERMINANT' )
    df_substance = df[['number_with_outcome']].where( df.topic == 'SUBSTANCE USE' )
    
    fig,axs = plt.subplots( 3, 3, figsize=(10,8), tight_layout=False )
    
    axs[0,0].scatter( df[['year']], df_access, alpha=0.5, color='b' )
    axs[0,0].set_xlabel('Access to care')
    
    axs[0,1].scatter( df[['year']], df_death, alpha=0.5, color='r' )
    axs[0,1].set_xlabel('Death')
    
    axs[0,2].scatter( df[['year']], df_dental, alpha=0.5, color='g' )
    axs[0,2].set_xlabel('Dental')
    
    axs[1,0].scatter( df[['year']], df_healthcond, alpha=0.5, color='r' )
    axs[1,0].set_xlabel('Health condition')
    
    axs[1,1].scatter( df[['year']], df_healthbehav, alpha=0.5, color='g' )
    axs[1,1].set_xlabel('Health behavior')
    
    axs[1,2].scatter( df[['year']], df_nutrition, alpha=0.5, color='b' )
    axs[1,2].set_xlabel('Nutrition')
    
    axs[2,0].scatter( df[['year']], df_safety, alpha=0.5, color='r' )
    axs[2,0].set_xlabel('Safety')
    
    axs[2,1].scatter( df[['year']], df_socialdeterm, alpha=0.5, color='g' )
    axs[2,1].set_xlabel('Social determinants')
    
    axs[2,2].scatter( df[['year']], df_substance, alpha=0.5, color='g' )
    axs[2,2].set_xlabel('Substance use')
    
    fig.supxlabel('Year')
    fig.supylabel('Number of cases with outcome')
    
    plt.show()