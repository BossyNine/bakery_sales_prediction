# Model Definition and Evaluation

## Selected Model and Implementation
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

## Hyperparameter Tuning

```Python
BATCH_SIZE = 16
LEARNING_RATE = 0.0001
MOMENTUM = 0.2
SEED = 1337
LOSS = 'mse'
COLS_TO_DROP = ['Umsatz']
```

Tuning mostly consist of minimal changes to the learning rate and the batch size. Huges improvments from moving from mape to mse.

## Evaluation and Optimizer

```Python
    # compile model
    opta = tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE)
    opts = tf.keras.optimizers.SGD(learning_rate=LEARNING_RATE, momentum=MOMENTUM)
    model.compile(optimizer=opta, loss=LOSS, metrics=['mae', 'mape'])

```

First SGD seems to produce better results, but in the end ADAM was better at optimizing the validation mape, which was just for sanity checking.
