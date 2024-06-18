import numpy as np
import pandas as pd
import os
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Const Parameters

BATCH_SIZE = 8
LEARNING_RATE = 0.005
MOMENTUM = 0.3
SEED = 123
LOSS = 'mape'
COLS_TO_DROP = ['Umsatz']


def main(input_path, output_path, epo=100):
    EPOCHS = epo
    # import data from ../sourcedata/cleaned_data/10_scaled_data.csv
    data = pd.read_csv(input_path)


    # split data into features and target
    features = data.drop(columns=COLS_TO_DROP)
    target = data['Umsatz']

    # split data into train and test
    features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=SEED)

    # reshape data for LSTM
    features_train = np.array(features_train)
    features_test = np.array(features_test)

    features_train_scaled = np.reshape(features_train, (features_train.shape[0], 1, features_train.shape[1]))
    features_test_scaled = np.reshape(features_test, (features_test.shape[0], 1, features_test.shape[1]))

    print(features_train_scaled.shape)
    print(features_test_scaled.shape)

    # define model
    model = Sequential()
    
    model.add(tf.keras.layers.InputLayer(shape=(features_train_scaled.shape[1], features_train_scaled.shape[2])))
    model.add(LSTM(features_train_scaled.shape[2], activation='relu', return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(features_train_scaled.shape[2], activation='relu', return_sequences=False))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1))


    print(model.summary())

    # compile model
    opta = tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE)
    opts = tf.keras.optimizers.SGD(learning_rate=LEARNING_RATE, momentum=MOMENTUM)
    model.compile(optimizer=opts, loss=LOSS)

    # fit model
    history = model.fit(features_train_scaled, target_train, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_data=(features_test_scaled, target_test))

    # save model
    model.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python model.py <input_path> <model_path> <epochs>")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    try:
        epo = int(sys.argv[3])
    except Exception as e:
        print("Cant cast epochs to int")
        sys.exit(1)

    main(input_path, output_path, epo)
