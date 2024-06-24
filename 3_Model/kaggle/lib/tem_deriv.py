import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer

def tempd(df):
    # Step 1: Calculate the 7-day rolling average for temperature
    df['temp_7d_avg'] = df['Temperatur'].rolling(window=7).mean()

    # Step 2: Fill NA values created by rolling average
    df['temp_7d_avg'].fillna(method='bfill', inplace=True)

    # Step 3: Calculate the difference for the next day
    df['temp_diff_next_day'] = df['Temperatur'].shift(-1) - df['temp_7d_avg']

    # Step 4: Create 'warmer than week before' and 'colder than week before' columns
    df['warmer_than_week_before'] = df['temp_diff_next_day'].apply(lambda x: x if x > 0 else 0)
    df['colder_than_week_before'] = df['temp_diff_next_day'].apply(lambda x: -x if x < 0 else 0)
    
    return df