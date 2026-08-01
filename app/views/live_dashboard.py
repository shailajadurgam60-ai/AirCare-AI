import streamlit as st
from datetime import datetime

from api import get_coordinates, get_live_aqi_and_pollutants

from advisory import get_health_advisory


from utils import (
    load_data,
    get_live_aqi_label,
    get_live_aqi_message,
    get_pollutant_status
)
def show_live_dashboard():
    df = load_data()

    cities = sorted(df["City"].unique())

   

    st.divider()

    st.subheader("📍 Select Location")

    city = st.selectbox(
    "Choose a City",
    cities
    )

    st.caption(
    "Select an Indian city to view its current air quality."
    )

    st.divider()
    with st.form("live_aqi_form"):

     submit = st.form_submit_button(
        "🔄 Get Live Air Quality"
    )
    if submit:
          try:
            with st.spinner("🌍 Fetching live air quality from OpenWeather API..."):

                lat, lon = get_coordinates(city)

            if lat is None or lon is None:

              st.warning(
              f"⚠️ Live air quality data is currently unavailable for **{city}**."
               )

              st.info(
              "Please select another city. Historical data is still available."
                )

              st.stop()

            with st.spinner("🌿 Retrieving live AQI..."):

              api_aqi, pollutants = get_live_aqi_and_pollutants(lat, lon)
            aqi_label = get_live_aqi_label(api_aqi)
            aqi_message = get_live_aqi_message(api_aqi)
    
            st.divider()
    
            st.subheader("📊 Live Air Quality")
    
            from datetime import datetime
    
            col1, col2, col3 = st.columns(3)
    
            with col1:
                st.metric(
                    label="AQI",
                    value=api_aqi
                )
    
            with col2:
                st.metric(
                    label="Category",
                    value=aqi_label
                )
    
            with col3:
                st.metric(
                    label="Last Updated",
                    value=datetime.now().strftime("%d %b %Y")
                )
    
            st.success(aqi_message)
    
           
    
            st.subheader("🧪 Live Pollutant Levels")
    
            pollutant_info = [
        ("PM2.5", "pm2_5"),
        ("PM10", "pm10"),
        ("CO", "co"),
        ("NO", "no"),
        ("NO₂", "no2"),
        ("SO₂", "so2"),
        ("O₃", "o3"),
        ("NH₃", "nh3"),
            ]
    
            cols = st.columns(4)
    
            for i, (label, key) in enumerate(pollutant_info):
    
               with cols[i % 4]:
                  with st.container(border=True):
    
                    st.metric(label, f"{pollutants[key]:.2f}")
                    st.caption("μg/m³")
                    st.caption(
                    get_pollutant_status(
                        key,
                        pollutants[key]
                    )
                )
    
            st.divider()
            st.caption("Live pollutant concentrations retrieved from the OpenWeather Air Pollution API.")
            st.divider()
    
            st.subheader("🩺 Personalized Health Advisory")
    
            advisory = get_health_advisory(api_aqi)
            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)
            with col1:
              with st.container(border=True):
                 st.markdown("### 👨 General Public")
                 st.write(advisory["General Public"])
            with col2:
              with st.container(border=True):
                 st.markdown("### 👶 Children")
                 st.write(advisory["Children"])
            with col3:
              with st.container(border=True):
                 st.markdown("### 👴 Elderly")
                 st.write(advisory["Elderly"])
            with col4:
              with st.container(border=True):
                 st.markdown("### 🫁 Respiratory Patients")
                 st.write(advisory["Respiratory Patients"])
    
          except Exception as e:

              st.exception(e)
    st.divider()
   
    
