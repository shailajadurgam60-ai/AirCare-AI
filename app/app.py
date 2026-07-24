import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AirCare AI",
    page_icon="🌿",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🌿 AirCare AI")

st.sidebar.info(
    """
    AirCare AI is a Machine Learning application
    that predicts Air Quality Index (AQI) and
    provides personalized health recommendations.
    """
)

# -----------------------------
# Main Title
# -----------------------------
st.title("🌍 AirCare AI")
st.subheader("Personalized Air Pollution Health Risk Advisor")

st.markdown("---")

# -----------------------------
# About Project
# -----------------------------
st.header("About")

st.write(
    """
    AirCare AI predicts the Air Quality Index (AQI)
    using machine learning based on air pollutant
    concentrations.

    The application also provides:

    - AQI Prediction
    - Health Risk Assessment
    - Personalized Precautions
    - Air Quality Insights
    """
)

st.markdown("---")
from datetime import date
from utils import (
    load_data,
    load_model,
    load_city_encoder,
    load_season_encoder,
    load_feature_columns,
    prepare_input,
    get_aqi_category

)
df = load_data()

model = load_model()

city_encoder = load_city_encoder()

season_encoder = load_season_encoder()

feature_columns = load_feature_columns()


# -----------------------------
# Placeholder
# -----------------------------
#User Inputs 
cities = sorted(df["City"].unique())
st.header("AQI Prediction")

with st.form("prediction_form"):

    city = st.selectbox(
        "🏙️ Select City",
        cities
    )

    selected_date = st.date_input(
        "📅 Select Date",
        value=date.today()
    )

    col1, col2 = st.columns(2)

    with col1:
        pm25 = st.number_input(
            "PM2.5 (µg/m³)",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

        pm10 = st.number_input(
            "PM10 (µg/m³)",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

        no = st.number_input(
            "NO (µg/m³)",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

        no2 = st.number_input(
            "NO₂ (µg/m³)",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

        nox = st.number_input(
            "NOx (µg/m³)",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

        nh3 = st.number_input(
            "NH₃ (µg/m³)",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

    with col2:
        co = st.number_input(
            "CO (mg/m³)",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

        so2 = st.number_input(
            "SO₂ (µg/m³)",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

        o3 = st.number_input(
            "O₃ (µg/m³)",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

        benzene = st.number_input(
            "Benzene (µg/m³)",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

        toluene = st.number_input(
            "Toluene (µg/m³)",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

    submit = st.form_submit_button("🔮 Predict AQI")
    if submit:
        input_data = prepare_input(
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
        )

        prediction = model.predict(input_data)[0]

        category = get_aqi_category(prediction)

        st.metric(
        label="🌿 Predicted AQI",
        value=f"{prediction:.2f}"
        )

        if category == "Good":
          st.success(f"🟢 AQI Category: {category}")

        elif category == "Satisfactory":
          st.info(f"🟡 AQI Category: {category}")

        elif category == "Moderate":
          st.warning(f"🟠 AQI Category: {category}")

        elif category == "Poor":
          st.error(f"🔴 AQI Category: {category}")

        elif category == "Very Poor":
          st.error(f"🟣 AQI Category: {category}")

        else:
          st.error(f"⚫ AQI Category: {category}")
        

