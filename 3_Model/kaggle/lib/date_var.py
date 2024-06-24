# import packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer

def get_season(month):
	if month in [12, 1, 2]:
	    return 'winter', 4
	elif month in [3, 4, 5]:
	    return 'spring', 1
	elif month in [6, 7, 8]:
	    return 'summer', 2
	else:
	    return 'autumn', 3

def date_var(df):
    df_w = df.copy()

    df_w['Datum'] = pd.to_datetime(df_w['Datum'], errors='coerce')
    df_w['year'] = df_w['Datum'].dt.year
    df_w['month'] = df_w['Datum'].dt.month
    df_w['week'] = df_w['Datum'].dt.isocalendar().week
    df_w['weekday'] = df_w['Datum'].dt.dayofweek
    df_w['day_month'] = df_w['Datum'].dt.day
    
    df_w['season_str'], df_w['season'] = zip(*df_w['month'].apply(get_season))
	
    return df_w