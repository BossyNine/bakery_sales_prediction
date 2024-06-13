import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Const Parameters
EPOCHS = 10
BATCH_SIZE = 32
LEARNING_RATE = 0.001
SEED = 123


def main():
    # import data 
    df = pd.read_csv('../sourcedata/cleaned_data/8_encoded_variables.csv')

    # convert Bewölkung into numeric
    df = pd.get_dummies(df, columns=['Bewoelkung'])

    # split data into features and target
    features = df.drop(columns=['Umsatz'])
    target = df['Umsatz']

    # extract number of features
    n_features = features.shape[1]

    print(n_features)

