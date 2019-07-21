from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from sklearn.model_selection import train_test_split

from keras.models import model_from_json

import os
import sys
import sklearn
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

sys.path.append('..')

def predict_rate(rate_for_past_sixty_days, number_of_predicted_days = 14):
    # load trained LSTM
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)

    # load weights into new model
    model.load_weights("model.h5")
    print("Loaded model from disk")

    # scale data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(rate_for_past_sixty_days.values)

    # make prediction
    input_data = scaled_data.flatten().tolist()[-60:]
    input_data_as_np = np.asarray(input_data).reshape((1, len(input_data), 1))

    predictions = []
    for i in range(number_of_predicted_days):
        prediction = model.predict(input_data_as_np)
        predictions.append(prediction[0, 0])

        updated_input = input_data_as_np.flatten().tolist()
        updated_input.append(prediction[0, 0])
        updated_input.pop(0)

        input_data_as_np = np.asarray(updated_input).reshape((1, len(updated_input), 1))

    predictionsnp = scaler.inverse_transform(np.asarray(predictions).reshape((len(predictions), 1)))
    a = predictionsnp.flatten().tolist()
    return a
