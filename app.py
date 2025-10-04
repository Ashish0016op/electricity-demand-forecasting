import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("electicity_xgb_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Electricity Demand Forecasting")

# Input fields for each feature
hour = st.number_input("Hour", min_value=0, max_value=23, step=1)
dayofweek = st.number_input("Day of Week (0=Monday, 6=Sunday)", min_value=0, max_value=6, step=1)
month = st.number_input("Month", min_value=1, max_value=12, step=1)
year = st.number_input("Year", min_value=2000, max_value=2100, step=1, value=2024)
dayofyear = st.number_input("Day of Year", min_value=1, max_value=366, step=1)
weekofyear = st.number_input("Week of Year", min_value=1, max_value=53, step=1)
quarter = st.number_input("Quarter", min_value=1, max_value=4, step=1)
is_weekend = st.number_input("Is Weekend (0=No, 1=Yes)", min_value=0, max_value=1, step=1)
temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
demand_lag_24hr = st.number_input("Demand Lag 24hr")
demand_lag_168hr = st.number_input("Demand Lag 168hr")
demand_rolling_mean_24hr = st.number_input("Demand Rolling Mean 24hr")
demand_rolling_std_24hr = st.number_input("Demand Rolling Std 24hr")

if st.button("Predict"):
    # Prepare the input as a 2D array (1 row, 14 columns)
    features = np.array([[
        hour, dayofweek, month, year, dayofyear, weekofyear, quarter, is_weekend,
        temperature, humidity, demand_lag_24hr, demand_lag_168hr,
        demand_rolling_mean_24hr, demand_rolling_std_24hr
    ]])
    prediction = model.predict(features)
    st.success(f"Predicted Electricity Demand: {prediction[0]:.2f}")