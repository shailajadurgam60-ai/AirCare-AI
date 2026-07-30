import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

def show_ml_insights():
    df = load_data()

    st.title("📊 Machine Learning Insights")

    st.markdown("""
Explore the dataset, model performance, and feature importance used by AirCare AI.
""")

    st.divider()
    st.subheader("📁 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
      st.metric("Records", len(df))

    with col2:
      st.metric("Cities", df["City"].nunique())

    with col3:
      st.metric("Years", "2015–2020")
    st.divider()

    st.subheader("🤖 Model Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
       st.metric("R² Score", "0.9142")

    with col2:
       st.metric("MAE", "20.23")

    with col3:
       st.metric("RMSE", "39.63")
    importance_df = pd.DataFrame({
    "Feature": [
        "PM2.5",
        "CO",
        "PM10",
        "NO",
        "City",
        "NO₂",
        "O₃",
        "SO₂",
        "Day",
        "Year",
        "Season",
        "Month",
        "NH₃"
    ],
    "Importance": [
        0.504792,
        0.381412,
        0.038944,
        0.028626,
        0.025400,
        0.006738,
        0.006724,
        0.004449,
        0.001054,
        0.000622,
        0.000498,
        0.000428,
        0.000313
    ]
})
    st.divider()

    st.subheader("⭐ Feature Importance")

    fig = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Random Forest Feature Importance"
    )

    fig.update_layout(
    yaxis={"categoryorder": "total ascending"},
    height=550
    )

    st.plotly_chart(fig, use_container_width=True)
    st.divider()

    st.subheader("🌍 AQI Category Distribution")

    aqi_counts = (
    df["AQI_Bucket"]
    .value_counts()
    .reset_index()
    )

    aqi_counts.columns = ["Category", "Count"]

    fig = px.pie(
    aqi_counts,
    names="Category",
    values="Count",
    title="Distribution of AQI Categories"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.divider()

    st.subheader("🏭 Average AQI by City")

    city_aqi = (
    df.groupby("City")["AQI"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
    )

    fig = px.bar(
    city_aqi,
    x="AQI",
    y="City",
    orientation="h",
    title="Top 10 Cities by Average AQI"
    )

    fig.update_layout(
    yaxis={"categoryorder": "total ascending"},
    height=500
    )

    st.plotly_chart(fig, use_container_width=True)
    st.divider()

    st.subheader("📌 Key Findings")

    st.success("""
• PM2.5 is the most influential feature for AQI prediction.

• Carbon Monoxide (CO) is the second most important predictor.

• The Random Forest model achieved an R² score of 0.9142,
indicating strong predictive performance.

• The model captures historical pollution patterns effectively
across multiple Indian cities.
    """)
