import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import joblib


# Load the trained model
model = joblib.load('gold_price_model.pkl')

# Streamlit app title
st.title('Gold Price Prediction App')

# Load the dataset (for the time series plot)
gold_data = pd.read_csv('gold_data_processed.csv')
gold_data['Date'] = pd.to_datetime(gold_data['Date'])

# Sidebar inputs
spx = st.number_input('SPX Value:', min_value=0.0, format="%.2f")
slv = st.number_input('SLV Value:', min_value=0.0, format="%.2f")

# Year select box
years = list(range(2000, 2101))
selected_year = st.selectbox('Select Year:', years, index=years.index(2025))

# Month select box
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
selected_month_name = st.selectbox('Select Month:', months)
selected_month = months.index(selected_month_name) + 1

# Prediction button
if st.button('Predict Gold Price'):
    input_data = np.array([[spx, slv, selected_year, selected_month]])
    prediction = model.predict(input_data)
    st.success(f'Predicted Gold Price: ${prediction[0]:.2f}')

    st.subheader('📈 Predicted Gold Price Over Time')
    # Create a new row with the predicted value and current date
    new_row = pd.DataFrame({
    'Date': [pd.to_datetime(f'{selected_year}-{selected_month}-01')],
    'GLD': [prediction[0]]
    })


    # Append the new row to the gold_data DataFrame
    gold_data_extended = pd.concat([gold_data, new_row], ignore_index=True)

    # Plot the extended data
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(gold_data_extended['Date'], gold_data_extended['GLD'], color='gold')
    ax.set_xlabel('Date')
    ax.set_ylabel('Gold Price (GLD)')
    ax.set_title('Gold Price Trend with Predicted Value')
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)
else:
    st.subheader('📈 Gold Price Trend Over Time')

    # Plot the extended data
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.plot(gold_data['Date'], gold_data['GLD'], color='gold')
    ax.set_xlabel('Date')
    ax.set_ylabel('Gold Price (GLD)')
    ax.set_title('Gold Price Trend Over Time')
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)
