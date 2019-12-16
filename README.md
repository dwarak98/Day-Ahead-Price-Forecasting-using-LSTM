Day-Ahead-Price-Forecasting-using-LSTM
=======================================
Implemented Multivariate LSTM for predicting Day-Ahead Prices using State of the art libraries for deep learning.

## Content
- [Introduction](README.md#Introduction)
- [Model Architecture](README.md#Model-Architecture)
  - [Bidirectional LSTM Layer](README.md#Bidirectional-LSTM-Layer)
  - [Time Distribution Layer](README.md#Time-Distribution-Layer)
- [LSTM Model Parameters](README.md#LSTM-Model-Training)
- [Results](README.md#Results)


## Introduction
Accurately predicting day-ahead prices in the energy
service markets can significantly improve bidding strategies
for participating energy resources in the day-ahead energy
markets to generate higher revenues and optimize their
short-term operational planning. The day-ahead energy
service prices are highly dependent on energy demands or
load forecasting, renewable generation resources, which in turn are highly affected by weather
forecasting and other meteorological features. Hence, the
model needs to complex enough to capture the relationship
between different features and their higher-order terms to
generate even reasonable predictions. Using raw values of historical energy prices for uni-variate
and hourly load consumption for multi-variate model, we
create a new training set within the prediction sequence. As
a result, we predict day-ahead hourly energy prices using all
the lagged energy prices/load consumption values from input
sequence. 

## Model Architecture

<p align="center">
    <img width="480" height="300" src=model_arch.png>
</p>

## Bidirectional LSTM Layer
LSTM in general are used to store long term dependencies or patterns in the time series data. A bidirectional LSTM is a type of LSTM where there is two factor learning, one in the forward direction and the other in the reverse direction. In our case, we learn the price sequence from 1 to 24 hours and in the opposite direction. Bidirectional LSTM produces a better accuracy than unidirectional LSTM.  

## Time Distribution Layer


## LSTM Model Training

The training time for 20 epochs is around 30-40 minutes on google colab GPU. Once the model is trained, it is validated using validation dataset. Hyperparameter tuning of the model is critical task and this takes very long time compared to traditional forecasting techniques like ARIMA. Once we use a model to predict for the Day-Ahead, we cannot use the same model for future predictions, because we have to retrain the model with the most recent data to get a better accuracy. Deep learning models are not there yet for time series forecasting. When I can run ARIMA/ARIMAX for 2 minutes and get a equivalent result, there is a lot of savings on energy consumption and carbon footprint.   

In the model training, we observed the following: 

1. Number of epochs for training is not important. 
2. Batch size greatly influenced the predictions. Lower the batch size, better is the MAPE. 
3. Changing the structure of the network did not influence the results significantly.
![MODEL PARAMETERS](model_parameters.PNG)
<p align="center">
    <img width="480" height="300" src=learning_curve.PNG>
</p>

## Results

<p align="center">
    <img width="480" height="300" src=Predictions.PNG>
    
</p>


### MAPE (%) for different models

| Forecast Period |  LSTM | ARIMA | Linear Regression |
|:---------------:|:-----:|:-----:|:-----------------:|
|     48 Hour     | 20.64 |  5.8  |         -         |
|     24 Hour     |  6.55 |  4.52 |       12.95       |
|     12 Hour     |  3.24 |  2.85 |       12.86       |
|      4 Hour     |  1.35 |  2.21 |       12.66       |

***Note: Please find the attached report for more details regarding Linear Regression or ARIMA model***



