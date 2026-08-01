import streamlit as st
import pandas as pd
import joblib
import plotly.express as px


from views.live_dashboard import show_live_dashboard
from views.historical_prediction import show_historical_prediction
from views.ml_insights import show_ml_insights
from views.about import show_about
from components.footer import show_footer
# -----------------------------
# Page Configuration
# -----------------------------
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent
logo = Image.open(BASE_DIR / "assets" / "logo.png")

col1, col2 = st.columns([1, 6])

with col1:
    st.image(logo, width=90)

with col2:
    st.title("AirCare AI")
    st.caption("Intelligent Air Quality Monitoring & Health Advisory System")
# -----------------------------
# Side bar title
# -----------------------------
st.sidebar.image(logo, width=70)

st.sidebar.markdown("# 🌿 AirCare AI")

st.sidebar.caption("Intelligent Air Quality Monitoring")

st.sidebar.divider()

st.sidebar.markdown("### 🧭 Navigation")

page = st.sidebar.radio(
    "",
    [
        "🏠 Live Air Quality",
        "🤖 Historical Prediction",
        "📊 ML Insights",
        "ℹ️ About"
    ]
)

st.sidebar.divider()

st.sidebar.caption("Version 1.0")
if page == "🏠 Live Air Quality":
    show_live_dashboard()
    show_footer()

elif page == "🤖 Historical Prediction":
    show_historical_prediction()
    show_footer()

elif page == "📊 ML Insights":
    show_ml_insights()
    show_footer()

else:
    show_about()
    show_footer()
    # About section
# ==========================================
# PAGE HEADER
# ==========================================




