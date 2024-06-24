import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import sys

def encode_id(df):
    # Define categorical features
    categorical_features = ['Wettercode', 'KielerWoche', 'Warengruppe', 'Feiertage', 'Ferientage', 'Wetterklasse', 'year', 'month', 'weekday', 'day_month', 'season', 'Bewoelkung']

    for col in categorical_features:
        df[col] = df[col].astype('category')
    
    features = pd.get_dummies(df[categorical_features], drop_first=True, dtype=float)

    features[['id', 'Temperatur', 'Niederschlag', 'Windgeschwindigkeit', 'temp_diff_next_day']] = df[['id', 'Temperatur', 'Niederschlag', 'Windgeschwindigkeit', 'temp_diff_next_day']]

    scaler = MinMaxScaler()
    features[['Temperatur', 'Niederschlag', 'Windgeschwindigkeit', 'temp_diff_next_day']] = scaler.fit_transform(features[['Temperatur', 'Niederschlag', 'Windgeschwindigkeit', 'temp_diff_next_day']])

    return features

def encode_rev(df):
    # Define categorical features
    categorical_features = ['Wettercode', 'KielerWoche', 'Warengruppe', 'Feiertage', 'Ferientage', 'Wetterklasse', 'year', 'month', 'weekday', 'day_month', 'season', 'Bewoelkung']

    for col in categorical_features:
        df[col] = df[col].astype('category')
    
    features = pd.get_dummies(df[categorical_features], drop_first=True, dtype=float)

    features[['Umsatz', 'Temperatur', 'Niederschlag', 'Windgeschwindigkeit', 'temp_diff_next_day']] = df[['Umsatz', 'Temperatur', 'Niederschlag', 'Windgeschwindigkeit', 'temp_diff_next_day']]

    scaler = MinMaxScaler()
    features[['Temperatur', 'Niederschlag', 'Windgeschwindigkeit', 'temp_diff_next_day']] = scaler.fit_transform(features[['Temperatur', 'Niederschlag', 'Windgeschwindigkeit', 'temp_diff_next_day']])

    return features