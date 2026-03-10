import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.joblib")

st.title("🚲 Bike Rental Prediction App")

st.write(
    "This app predicts the number of bike rentals based on weather and time conditions."
)

st.header("Input Features")

# Categorical inputs
season = st.selectbox(
    "Season",
    [1, 2, 3, 4],
    format_func=lambda x: ["Spring", "Summer", "Fall", "Winter"][x-1]
)

yr = st.selectbox("Year", [0, 1], format_func=lambda x: "2011" if x == 0 else "2012")

mnth = st.slider("Month", 1, 12, 6)

hr = st.slider("Hour of the day", 0, 23, 12)

holiday = st.selectbox("Holiday", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

weekday = st.slider("Weekday", 0, 6, 3)

workingday = st.selectbox("Working day", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

weathersit = st.selectbox(
    "Weather Situation",
    [1, 2, 3],
    format_func=lambda x: {
        1: "Clear / Few clouds",
        2: "Mist / Cloudy",
        3: "Light Snow / Rain"
    }[x]
)

# Weather inputs
temp = st.slider("Temperature (normalized)", 0.0, 1.0, 0.5)

atemp = st.slider("Feeling Temperature (normalized)", 0.0, 1.0, 0.5)

hum = st.slider("Humidity", 0.0, 1.0, 0.5)

windspeed = st.slider("Wind Speed", 0.0, 1.0, 0.2)

# Prediction
if st.button("Predict Bike Rentals"):

    data = pd.DataFrame({
        "season": [season],
        "yr": [yr],
        "mnth": [mnth],
        "hr": [hr],
        "holiday": [holiday],
        "weekday": [weekday],
        "workingday": [workingday],
        "weathersit": [weathersit],
        "temp": [temp],
        "atemp": [atemp],
        "hum": [hum],
        "windspeed": [windspeed]
    })

    prediction = model.predict(data)

    st.subheader("Prediction Result")

    st.success(f"Estimated bike rentals: **{int(prediction[0])} bikes** 🚲")