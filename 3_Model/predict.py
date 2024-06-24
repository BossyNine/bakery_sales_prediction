import numpy as np
import pandas as pd
import sys
import os
from time import sleep
# set logging level
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow import keras

def main(data_to_predict_path, encoded_path, model_path):
    # check if files exist
    if not os.path.isfile(data_to_predict_path):
        print('To predicted data file not found')
        sys.exit(1)

    if not os.path.isfile(encoded_path):
        print('Library file not found')
        sys.exit(1)

    if not os.path.isfile(model_path):
        print('Model file not found')
        sys.exit(1)

    # load data
    try:
        data = pd.read_csv(data_to_predict_path)

    except Exception as e:
        print('Error loading data: ', e)
        sys.exit(1)
    
    # load library
    try:
        library = pd.read_csv(encoded_path)

    except Exception as e:
        print('Error loading library: ', e)
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

    data['id'] = data['id'].astype(float)
    library['id'] = library['id'].astype(float)

    # save rows of library with matching 'id' from data
    data_pre = library[library['id'].isin(data['id'])]

    # convert and reshape data
    data_pre = data_pre.drop(columns=['id'])
    data_pre = np.array(data_pre)
    data_pre = np.reshape(data_pre, (data_pre.shape[0], 1, data_pre.shape[1]))

    # predict
    try:
        predictions = model.predict(data_pre)
        print('Predictions: ', predictions)

    except Exception as e:
        print('Error predicting data: ', e)
        sys.exit(1)
    
    predictions = predictions.flatten()
    # save predictions in sample_submission.csv in column 'Umsatz'
    data['Umsatz'] = predictions
    data.to_csv('sample_submission.csv', index=False)
    print('Predictions saved')


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python predict.py <to_predict_path> <library_path> <model_path>')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])