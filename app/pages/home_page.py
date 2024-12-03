import warnings
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt




warnings.filterwarnings("ignore")


def home_page():
    if not st.session_state.get("logged_in"):
        st.error("Por favor, inicia sesión para acceder a esta página.")
        st.session_state.page = "login"
        st.rerun()

    if st.button("Cerrar sesión"):
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.rerun()
    

    ticker = st.text_input("Etiqueta de cotización", "EA")
    st.write(f"La etiqueta de cotización actual es: **{ticker}**")

    tic = yf.Ticker(ticker)
    hist = tic.history(period="5y", auto_adjust=True)

    st.write("Datos históricos")
    st.dataframe(hist)

    df = hist.copy()
    data = df.filter(['Close'])
    dataset = data.values
    training_data_len = int(np.ceil( len(dataset) * .95 ))




    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(dataset)

    train_data = scaled_data[0:int(training_data_len), :]
    x_train = []
    y_train = []

    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i, 0])
        y_train.append(train_data[i, 0])
        if i<= 61:
            print(x_train)
            print(y_train)
            print()
            
    x_train, y_train = np.array(x_train), np.array(y_train)

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    model = Sequential()
    model.add(LSTM(64, return_sequences=True, input_shape= (x_train.shape[1], 1)))
    model.add(LSTM(32, return_sequences=False))
    model.add(Dense(12))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')

    model.fit(x_train, y_train, batch_size=1, epochs=1)
    test_data = scaled_data[training_data_len - 60: , :]
    x_test = []
    y_test = dataset[training_data_len:, :]
    for i in range(60, len(test_data)):
        x_test.append(test_data[i-60:i, 0])
        
    x_test = np.array(x_test)

    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1 ))

    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)

    rmse = np.sqrt(np.mean(((predictions - y_test) ** 2)))

    train = data[:training_data_len]
    valid = data[training_data_len:]
    valid['Predictions'] = predictions
    plt.figure(figsize=(16,6))
    plt.title('Model')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.plot(train['Close'])
    plt.plot(valid[['Close', 'Predictions']])
    plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
    plt.show()
    st.pyplot(plt)
