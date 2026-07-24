import joblib
import pandas as pd
import streamlit as st

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("../data/processed/clean_air_quality.csv")


# -------------------------------
# Load ML Model
# -------------------------------
@st.cache_resource
def load_model():
    return joblib.load("/home/user/Documents/MLModels/aircare_rf_model.pkl")


# -------------------------------
# Load Encoders
# -------------------------------
import os

@st.cache_resource

@st.cache_resource
def load_city_encoder():
    return joblib.load("../models/label_encoder_city.pkl")


@st.cache_resource
def load_season_encoder():
    return joblib.load("../models/label_encoder_season.pkl")

@st.cache_resource
def load_feature_columns():
    return joblib.load("../models/feature_columns.pkl")


from datetime import datetime


def get_season(month):
    """Return season based on month."""
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Summer"
    elif month in [6, 7, 8, 9]:
        return "Monsoon"
    else:
        return "Post-Monsoon"


def prepare_input(
    selected_date,
    city,
    pm25,
    pm10,
    no,
    no2,
    nox,
    nh3,
    co,
    so2,
    o3,
    benzene,
    toluene,
    city_encoder,
    season_encoder,
    feature_columns
):

    year = selected_date.year
    month = selected_date.month
    day = selected_date.day

    season = get_season(month)

    city_encoded = city_encoder.transform([city])[0]
    season_encoded = season_encoder.transform([season])[0]

    input_df = pd.DataFrame([{
    "City": city_encoded,
    "PM2.5": pm25,
    "PM10": pm10,
    "NO": no,
    "NO2": no2,
    "NOx": nox,
    "NH3": nh3,
    "CO": co,
    "SO2": so2,
    "O3": o3,
    "Benzene": benzene,
    "Toluene": toluene,
    "Year": year,
    "Month": month,
    "Day": day,
    "Season": season_encoded
    }])

    input_df = input_df[feature_columns]

    return input_df[feature_columns]
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"
