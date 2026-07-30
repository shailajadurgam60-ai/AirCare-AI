import joblib
import pandas as pd
import streamlit as st

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("../data/processed/clean_air_quality.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df


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
import pandas as pd


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
    city,
    pollutants,
    city_encoder,
    season_encoder,
    feature_columns,
    date=None
):
    """
    Prepare model input using live pollutant data.
    """

    if date is None:
     date = datetime.now()

    year = date.year
    month = date.month
    day = date.day

    season = get_season(month)

    city_encoded = city_encoder.transform([city])[0]
    season_encoded = season_encoder.transform([season])[0]

    input_df = pd.DataFrame([{
        "City": city_encoded,
        "PM2.5": pollutants["pm2_5"],
        "PM10": pollutants["pm10"],
        "NO": pollutants["no"],
        "NO2": pollutants["no2"],
        "NH3": pollutants["nh3"],
        "CO": pollutants["co"],
        "SO2": pollutants["so2"],
        "O3": pollutants["o3"],
        "Year": year,
        "Month": month,
        "Day": day,
        "Season": season_encoded
    }])

    return input_df[feature_columns]
def get_aqi_category(aqi):
    """
    Return AQI category based on the predicted AQI value.
    """

    if aqi <= 50:
        return "Good 🟢"

    elif aqi <= 100:
        return "Satisfactory 🟡"

    elif aqi <= 200:
        return "Moderately Polluted 🟠"

    elif aqi <= 300:
        return "Poor 🔴"

    elif aqi <= 400:
        return "Very Poor 🟣"

    else:
        return "Severe ⚫"
def get_live_aqi_label(api_aqi):
    mapping = {
        1: "Good 🟢",
        2: "Fair 🟡",
        3: "Moderate 🟠",
        4: "Poor 🔴",
        5: "Very Poor ⚫",
    }
    return mapping.get(api_aqi, "Unknown")


def get_live_aqi_message(api_aqi):
    if api_aqi == 1:
        return "Air quality is good. Normal outdoor activities are fine."
    elif api_aqi == 2:
        return "Air quality is fair. Sensitive people should watch for symptoms."
    elif api_aqi == 3:
        return "Air quality is moderate. Reduce prolonged outdoor exertion if possible."
    elif api_aqi == 4:
        return "Air quality is poor. Limit outdoor activity and stay alert."
    elif api_aqi == 5:
        return "Air quality is very poor. Stay indoors as much as possible."
    return "AQI level unavailable."
def get_pollutant_status(pollutant, value):

    limits = {
        "pm2_5": [(15, "🟢 Excellent"),
                  (35, "🟡 Moderate"),
                  (75, "🟠 Poor"),
                  (float("inf"), "🔴 Very Poor")],

        "pm10": [(50, "🟢 Excellent"),
                 (100, "🟡 Moderate"),
                 (250, "🟠 Poor"),
                 (float("inf"), "🔴 Very Poor")],

        "co": [(4400, "🟢 Excellent"),
               (9400, "🟡 Moderate"),
               (12400, "🟠 Poor"),
               (float("inf"), "🔴 Very Poor")],

        "no2": [(40, "🟢 Excellent"),
                (80, "🟡 Moderate"),
                (180, "🟠 Poor"),
                (float("inf"), "🔴 Very Poor")],

        "so2": [(40, "🟢 Excellent"),
                (80, "🟡 Moderate"),
                (380, "🟠 Poor"),
                (float("inf"), "🔴 Very Poor")],

        "o3": [(60, "🟢 Excellent"),
               (100, "🟡 Moderate"),
               (180, "🟠 Poor"),
               (float("inf"), "🔴 Very Poor")],

        "nh3": [(200, "🟢 Excellent"),
                (400, "🟡 Moderate"),
                (800, "🟠 Poor"),
                (float("inf"), "🔴 Very Poor")],

        "no": [(40, "🟢 Excellent"),
               (80, "🟡 Moderate"),
               (180, "🟠 Poor"),
               (float("inf"), "🔴 Very Poor")]
    }

    for threshold, status in limits[pollutant]:
        if value <= threshold:
            return status

    return "Unknown"