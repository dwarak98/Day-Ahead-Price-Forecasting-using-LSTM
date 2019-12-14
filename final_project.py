# -*- coding: utf-8 -*-
"""Final_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U8K-i23UP4c76W9eL2Em5XdCpSqANk53
"""

from numpy import array
from keras.layers import Bidirectional, Flatten
from keras.layers.normalization import BatchNormalization
from oauth2client.client import GoogleCredentials
from google.colab import auth
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import GRU
from keras.layers import TimeDistributed
from keras.layers import Bidirectional
from keras.layers import Dropout
from keras.utils import to_categorical
import random

from google.colab import drive
drive.mount('/content/gdrive')

!pip install - U - q PyDrive

# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# Copy/download the file
fid = drive.ListFile({'q': "title='Final_project.ipynb'"}).GetList()[0]['id']
f = drive.CreateFile({'id': fid})
f.GetContentFile('Final_project.ipynb')

# Read price data and keep only required columns


def daprice_muiz():
    price_2 = pd.read_csv(
        '/content/gdrive/My Drive/Topics in Data Science/Final Project/Data Source/Price data/2019_2018_OASIS_Day-Ahead_Market_Zonal_LBMP.csv')
    price_1 = pd.read_csv(
        '/content/gdrive/My Drive/Topics in Data Science/Final Project/Data Source/Price data/2016_2017_OASIS_Day-Ahead_Market_Zonal_LBMP.csv')

    # price_2 = pd.read_csv('/content/gdrive/My Drive/ECE 592 Topics in Data Science/Final Project/Data Source/Price data/2019_2018_OASIS_Day-Ahead_Market_Zonal_LBMP.csv')
    # price_1 = pd.read_csv('/content/gdrive/My Drive/ECE 592 Topics in Data Science/Final Project/Data Source/Price data/2016_2017_OASIS_Day-Ahead_Market_Zonal_LBMP.csv')

    price_1.rename(columns={'Eastern Date Hour': 'Datetime', 'DAM Zonal LBMP': 'LBMP',
                            'DAM Zonal Losses': 'Losses', 'DAM Zonal Congestion': 'Congestion'}, inplace=True)
    p1 = price_1[['Datetime', 'LBMP', 'Losses', 'Congestion']].copy()

    price_2.rename(columns={'Eastern Date Hour': 'Datetime', 'DAM Zonal LBMP': 'LBMP',
                            'DAM Zonal Losses': 'Losses', 'DAM Zonal Congestion': 'Congestion'}, inplace=True)
    p2 = price_2[['Datetime', 'LBMP', 'Losses', 'Congestion']].copy()
    price_data = pd.concat([p1, p2], ignore_index=True)
    price_data

    load_2 = pd.read_csv(
        '/content/gdrive/My Drive/Topics in Data Science/Final Project/Data Source/Load data/2019_OASIS_Day_Ahead_Market_ISO_Load_Forecast.csv')
    load_1 = pd.read_csv(
        '/content/gdrive/My Drive/Topics in Data Science/Final Project/Data Source/Load data/2016_2017_OASIS_Day_Ahead_Market_ISO_Load_Forecast.csv')

    # load_2 = pd.read_csv('/content/gdrive/My Drive/ECE 592 Topics in Data Science/Final Project/Data Source/Load data/2019_OASIS_Day_Ahead_Market_ISO_Load_Forecast.csv')
    #load_1 = pd.read_csv('/content/gdrive/My Drive/ECE 592 Topics in Data Science/Final Project/Data Source/Load data/2016_2017_OASIS_Day_Ahead_Market_ISO_Load_Forecast.csv')

    load_1 = load_1[load_1['Zone Name'] == 'LONGIL'].copy()
    load_1.rename(columns={'Eastern Date Hour': 'Datetime',
                           'DAM Forecast Load': 'Forecasted_load'}, inplace=True)
    l1 = load_1[['Datetime', 'Forecasted_load']]

    load_2 = load_2[load_2['Zone Name'] == 'LONGIL'].copy()
    load_2.rename(columns={'Eastern Date Hour': 'Datetime',
                           'DAM Forecast Load': 'Forecasted_load'}, inplace=True)
    l2 = load_2[['Datetime', 'Forecasted_load']]

    load_data = pd.concat([l1, l2], ignore_index=True)
    load_data
    return price_data, load_data

# Read price data and keep only required columns


def daprice_dwarak():
    # price_2 = pd.read_csv('/content/gdrive/My Drive/Topics in Data Science/Final Project/Data Source/Price data/2019_2018_OASIS_Day-Ahead_Market_Zonal_LBMP.csv')
    # price_1 = pd.read_csv('/content/gdrive/My Drive/Topics in Data Science/Final Project/Data Source/Price data/2016_2017_OASIS_Day-Ahead_Market_Zonal_LBMP.csv')

    price_2 = pd.read_csv(
        '/content/gdrive/My Drive/ECE 592 Topics in Data Science/Final Project/Data Source/Price data/2019_2018_OASIS_Day-Ahead_Market_Zonal_LBMP.csv')
    price_1 = pd.read_csv(
        '/content/gdrive/My Drive/ECE 592 Topics in Data Science/Final Project/Data Source/Price data/2016_2017_OASIS_Day-Ahead_Market_Zonal_LBMP.csv')

    price_1.rename(columns={'Eastern Date Hour': 'Datetime', 'DAM Zonal LBMP': 'LBMP',
                            'DAM Zonal Losses': 'Losses', 'DAM Zonal Congestion': 'Congestion'}, inplace=True)
    p1 = price_1[['Datetime', 'LBMP', 'Losses', 'Congestion']].copy()

    price_2.rename(columns={'Eastern Date Hour': 'Datetime', 'DAM Zonal LBMP': 'LBMP',
                            'DAM Zonal Losses': 'Losses', 'DAM Zonal Congestion': 'Congestion'}, inplace=True)
    p2 = price_2[['Datetime', 'LBMP', 'Losses', 'Congestion']].copy()
    price_data = pd.concat([p1, p2], ignore_index=True)
    price_data

    load_2 = pd.read_csv(
        '/content/gdrive/My Drive/ECE 592 Topics in Data Science/Final Project/Data Source/Load data/2019_OASIS_Day_Ahead_Market_ISO_Load_Forecast.csv')
    load_1 = pd.read_csv(
        '/content/gdrive/My Drive/ECE 592 Topics in Data Science/Final Project/Data Source/Load data/2016_2017_OASIS_Day_Ahead_Market_ISO_Load_Forecast.csv')

    load_1 = load_1[load_1['Zone Name'] == 'LONGIL'].copy()
    load_1.rename(columns={'Eastern Date Hour': 'Datetime',
                           'DAM Forecast Load': 'Forecasted_load'}, inplace=True)
    l1 = load_1[['Datetime', 'Forecasted_load']]

    load_2 = load_2[load_2['Zone Name'] == 'LONGIL'].copy()
    load_2.rename(columns={'Eastern Date Hour': 'Datetime',
                           'DAM Forecast Load': 'Forecasted_load'}, inplace=True)
    l2 = load_2[['Datetime', 'Forecasted_load']]

    load_data = pd.concat([l1, l2], ignore_index=True)
    load_data
    return price_data, load_data


# merging data based on end-index date
price_data, load_data = daprice_dwarak()

end_index = load_data.index[load_data.Datetime == price_data.Datetime.iloc[-1]].tolist()
data = pd.merge(price_data, load_data[:end_index[0]+1], how='left', on='Datetime')

plt.plot(data.LBMP)
plt.plot(data.Losses)
plt.plot(data.Congestion)
plt.legend(['LBMP', 'Losses', 'Congestion'])
plt.title('LBMP Losses and Congestion over 4-year period')
plt.show()

plt.plot(data.Forecasted_load)
plt.title("Forecasted Load over 4-year period")
plt.show()


def create_model1(X):

    # define model
    model = Sequential()
    model.add(Bidirectional(LSTM(256, return_sequences=True,
                                 input_shape=(X.shape[0], X.shape[1], X.shape[2]))))
    #model.add(GRU(256, return_sequences=True, input_shape=(X.shape[1], X.shape[2])))

    # model.add(Bidirectional(LSTM(128)))
    model.add(TimeDistributed(Dense(64, activation='relu'),
                              input_shape=(None, X.shape[1], X.shape[2])))
    # # model.add(TimeDistributed(Dense(32, activation='relu')))
    # # model.add(TimeDistributed(Dense(1, activation = 'relu')))
    # # model.add(Dense(64, activation='relu'))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    # model.add(Dropout(0.3))
    #model.add(Dense(256, activation='relu'))
    #model.add(Dense(128, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.compile(optimizer='adam', loss=['mae'],  metrics=['mse', 'mape'])
    return model


def create_model(X):

    # define model
    model = Sequential()
    model.add(Bidirectional(LSTM(100, return_sequences=True,
                                 input_shape=(X.shape[0], X.shape[1], X.shape[2]))))
    #model.add(GRU(256, return_sequences=True, input_shape=(X.shape[1], X.shape[2])))

    # model.add(Bidirectional(LSTM(128)))
    model.add(TimeDistributed(Dense(128, activation='relu'),
                              input_shape=(None, X.shape[1], X.shape[2])))
   # model.add(TimeDistributed(Dense(64, activation='relu')))
   # model.add(TimeDistributed(Dense(32, activation='relu')))
    #model.add(TimeDistributed(Dense(5, activation = 'relu')))
    #model.add(Dense(64, activation='relu'))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.3))
    #model.add(Dense(256, activation='relu'))
    # model.add(Dropout(0.4))
    #model.add(Dense(128, activation='relu'))
    # model.add(Dropout(0.4))
    model.add(Dense(12, activation='relu'))
    model.compile(optimizer='adam', loss=['mape'],  metrics=['mse', 'mape'])
    return model

# split a multivariate sequence into samples


def split_sequence_multi(sequence, n_steps):
    lbmp = sequence.LBMP.values
    load = sequence.Forecasted_load.values
    X, y = list(), list()
    for i in range(124, len(sequence)):
        end_ix = i + n_steps
        if end_ix + n_steps > len(sequence):
            break
        T1 = [1, 2, 23, 24, 169, 170, 191, 192, 365, 366, 368, 376, 377, 378, 379]
        T = [1, 2, 23, 24, 25, 26, 27, 47, 48, 49, 70, 71, 72, 73,
             74, 75, 76, 93, 94, 95, 96, 97, 120, 121, 122, 123]
        q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
             15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        #q = [1,2,3,4,5,6,7,8,20,21,22,23,24,25,26]
        #
        seq_x1 = [[lbmp[i-t]] for t in T]
        seq_x2 = [[load[i-t]] for t in T]
        seq_x3 = [[lbmp[i]-lbmp[i-t]] for t in T]  # P term
        seq_x4 = [[lbmp[i-t]-lbmp[i-t-1]] for t in q]
        seq_x5 = [[load[i-t]-load[i-t-1]] for t in q]
        seq_y = lbmp[i:end_ix]
        X.append([seq_x3, seq_x4, seq_x5])
        y.append(seq_y)
    return (X), (y)

# split a multivariate sequence into samples


def split_sequence_multi_testdata(sequence, n_steps):
    lbmp = sequence.LBMP.values
    load = sequence.Forecasted_load.values
    X, y = list(), list()
    for i in range(len(sequence)-n_steps, len(sequence)-n_steps+1, 1):
        end_ix = i + n_steps
        if end_ix > len(sequence):
            break
        T1 = [1, 2, 23, 24, 169, 170, 191, 192, 365, 366, 368, 376, 377, 378, 379]
        T = [1, 2, 23, 24, 25, 26, 27, 47, 48, 49, 70, 71, 72, 73,
             74, 75, 76, 93, 94, 95, 96, 97, 120, 121, 122, 123]
        q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
             15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        #q = T
        seq_x1 = [[lbmp[i-t]] for t in T]
        seq_x2 = [[load[i-t]] for t in T]
        seq_x3 = [[lbmp[i]-lbmp[i-t]] for t in T]  # P term
        seq_x4 = [[lbmp[i-t]-lbmp[i-t-1]] for t in q]
        seq_x5 = [[load[i-t]-load[i-t-1]] for t in q]
        seq_y = lbmp[i:end_ix]
        X.append([seq_x3, seq_x4, seq_x5])
        y.append(seq_y)
    return (X), (y)

# split a univariate sequence into samples


def split_sequence_uni(sequence, n_steps):
    lbmp = sequence.LBMP.values
    load = sequence.Forecasted_load.values

    X, y = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the sequence
        if end_ix+n_steps > len(sequence)-1:
            break
        # gather input and output parts of the pattern
        seq_x1 = lbmp[i:end_ix]

        seq_y = lbmp[end_ix:(end_ix+n_steps)]
        X.append(seq_x1)
        y.append(seq_y)
    return (X), (y)

# split a univariate sequence into samples


def split_sequence_uni_test(sequence, n_steps):
    lbmp = sequence.LBMP.values
    load = sequence.Forecasted_load.values

    X, y = list(), list()
    for i in range(len(sequence)-2*n_steps, len(sequence)-2*n_steps+1, 1):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the sequence
        if end_ix > len(sequence)-1:
            break
        # gather input and output parts of the pattern
        seq_x1 = lbmp[i:end_ix]

        seq_y = lbmp[end_ix:(end_ix+n_steps)]
        X.append(seq_x1)
        y.append(seq_y)
    return (X), (y)


n_steps = 24
X, y = split_sequence_multi(data, n_steps)

X = np.asarray(X)
y = np.asarray(y)
print(X.shape)
print(y.shape)
# # reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 3
X = X.reshape((X.shape[0], X.shape[2], n_features))


#from sklearn.model_selection import train_test_split
#X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.01, random_state = 0)

model = create_model(X)

# fit model
history = model.fit(X, y, epochs=20, validation_split=0.25, batch_size=16)

plt.plot(history.history['loss'], label='Training Mape')
plt.plot(history.history['val_loss'], label='Validation Mape')
plt.xlabel('Epochs')
plt.ylabel('Mean Absolute Percentage Error')
plt.legend()
plt.show()

# n_steps = 4

X_test, y_test = split_sequence_multi_testdata(data, n_steps)
X_test = np.asarray(X_test)
y_test = np.asarray(y_test)
print(X_test)
print(y_test)
# # reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 3
X_test = X_test.reshape((X_test.shape[0], X_test.shape[2], n_features))

model.summary()


acc = model.evaluate(X_test, y_test)

prediction = model.predict(X_test)

print(acc)
print(prediction)

plt.plot(np.transpose(prediction), label="prediction")
plt.plot(np.transpose(y_test), label="Ground Truth")
plt.xlabel('Hours')
plt.ylabel('Day-Ahead LMP')
plt.legend()
plt.show()

model.fit(X, y, epochs=10, validation_split=0.25)

path = '/content/gdrive/My Drive/ECE 592 Topics in Data Science/Final Project/'
file = 'best_model_mape_6_35.h5'
model.save(path+file)
model_file = drive.CreateFile({'title': file})
model_file.SetContentFile(path+file)
model_file.Upload()
