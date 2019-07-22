import requests
import json
from datetime import date, timedelta
from prediction_function import predict_rate
import numpy as np
import pandas as pd

def get_currency_rates(base_currency, currency, start_date, end_date):
    # Get exchange rates
    url = f'https://api.exchangeratesapi.io/history?start_at={start_date}&end_at={end_date}&base={base_currency}&symbols={currency}'
    response = requests.get(url)
    code = response.status_code
    response_json = response.json()
    rates = response_json['rates']

    # Create dates list dictionary for the period
    dates_list = {}
    delta = end_date - start_date
    for i in range(delta.days + 1):
        dates_list[f'{start_date + timedelta(i)}'] = 0

    # Populate the periods with data from the API
    for key, value in rates.items():
        if key in dates_list:
            dates_list[key] = value[currency]

    # If there is no info for the day, average
    currency_list = [v for k, v in dates_list.items()]
    dates_list = [k for k, v in dates_list.items()]

    # Fix the missing values
    new_currency_list = []
    non_zero_value = 0
    for i, k in enumerate(currency_list):
        if k == 0:
            new_currency_list.append(non_zero_value)
        else:
            new_currency_list.append(k)
            non_zero_value = k

    if currency_list[1] == 0:
        new_currency_list[1] = new_currency_list[2]
    if currency_list[0] == 0:
        new_currency_list[0] = new_currency_list[1]

    # Predict new values
    data = np.asarray(new_currency_list[-60:])
    datapd = pd.DataFrame(data)
    predicted_data = predict_rate(datapd)

    predicted_data_fixed = []
    for i in range(0,len(new_currency_list)):
        predicted_data_fixed.append(new_currency_list[i])

    for i in range(0, len(predicted_data)):
        predicted_data_fixed.append(predicted_data[i])

    # Append new values
    for i in range(1,15):
        dates_list.append(f'{end_date + timedelta(i)}')

    return (new_currency_list[-30:], dates_list[-44:], predicted_data_fixed[-44:])
