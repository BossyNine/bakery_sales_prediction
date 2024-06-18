# Model Definition and Evaluation

The model is a simple NN with twi LSTM, two Dropout, three Dense and one Output Layer.

```python
   model.add(tf.keras.layers.InputLayer(shape=(features_train_scaled.shape[1], features_train_scaled.shape[2])))
    model.add(LSTM(features_train_scaled.shape[2], activation='relu', return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(features_train_scaled.shape[2], activation='relu', return_sequences=False))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(32, activation='rel
```

The `model.py`script expects a path for a .csv with normalized and numeric features, a path where to save the model and the number of epochs for training.

The `predict`script expects a path for a .csv with normalized and numeric features, a path where to load the model from and a string with the target feature in the data. It saves the prediction in the calling directory.

`final_prep.py`is just for final formatting of the data.