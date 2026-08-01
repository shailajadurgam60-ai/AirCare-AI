import os
import requests
import streamlit as st

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    try:
        API_KEY = st.secrets["OPENWEATHER_API_KEY"]
    except Exception:
        API_KEY = None
@st.cache_data(ttl=86400)
def get_coordinates(city):
    url = (
        f"https://api.openweathermap.org/geo/1.0/direct"
        f"?q={city},IN&limit=1&appid={API_KEY}"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not data:
        return None, None

    return data[0]["lat"], data[0]["lon"]

@st.cache_data(ttl=300)
def get_live_aqi_and_pollutants(lat, lon):

    url = (
        f"https://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}&lon={lon}&appid={API_KEY}"
    )

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()["list"][0]

    return data["main"]["aqi"], data["components"]
