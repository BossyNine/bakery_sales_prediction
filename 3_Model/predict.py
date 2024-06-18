# load keras pretrained model and predict time series data

import numpy as np
import pandas as pd
import sys
import os
from time import sleep

# set logging level
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow import keras

def main(data_path, model_path, target_name):
    # check if files exist
    if not os.path.isfile(data_path):
        print('Data file not found')
        sys.exit(1)

    if not os.path.isfile(model_path):
        print('Model file not found')
        sys.exit(1)

    # load data
    try:
        data = pd.read_csv(data_path)
        target = data[target_name]
        data = data.drop(columns=target_name)
        print("Data loaded")

    except Exception as e:
        print('Error loading data: ', e)
        sys.exit(1)

    # load model
    try:
        model = keras.models.load_model(model_path, compile=False)
        model.compile(optimizer='sgd', loss='mape')
        print('Model loaded')
        sleep(1)
        print(model.summary())

    except Exception as e:
        print('Error loading model: ', e)
        sys.exit(1)

    # convert and reshape data
    data = np.array(data)
    data = np.reshape(data, (data.shape[0], 1, data.shape[1]))
    target = np.array(target)
    target = np.reshape(target, (target.shape[0]))

    # predict
    try:
        predictions = model.predict(data)
        print('Predictions: ', predictions)
        print('Targets: ', target)

    except Exception as e:
        print('Error predicting data: ', e)
        sys.exit(1)

    #save predictions
    try:
        predictions.to_csv('predictions.csv')
        print('Predictions saved')
    
    except Exception as e:
        print('Unable to save predictions: ', e)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3 and len(sys.argv) > 4:
        print('Usage: python predict.py <data_path> <model_path> <target>')
        sys.exit(1)

    data_path = sys.argv[1]
    model_path = sys.argv[2]
    if len(sys.argv) == 4:
        target = sys.argv[3]
    target = 'Umsatz'

    main(data_path, model_path, target)
