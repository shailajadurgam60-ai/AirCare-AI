import streamlit as st
def show_about():

    st.title("🌿 About AirCare AI")

    st.markdown("""
### Intelligent Air Quality Monitoring & Health Advisory System

AirCare AI combines **Machine Learning**, **Real-Time Air Quality Monitoring**,
and **Personalized Health Recommendations** into a single interactive dashboard
to help users understand environmental conditions and make informed health decisions.
""")

    st.divider()
    st.subheader("🎯 Project Overview")

    st.write("""
Air pollution is one of the leading environmental health risks worldwide.
People often have access to AQI numbers but lack personalized insights into
what those values actually mean.

AirCare AI bridges this gap by integrating:

• Real-time AQI monitoring

• Historical AQI prediction using Machine Learning

• Pollutant visualization

• Personalized health advisory

• Interactive analytics dashboard
""")
    st.divider()

    st.subheader("✨ Features")

    col1, col2 = st.columns(2)

    with col1:

     st.success("""
✅ Live AQI Monitoring

✅ Live Pollutant Dashboard

✅ Personalized Health Advisory

✅ Historical AQI Prediction
""")

    with col2:

      st.success("""
✅ Machine Learning Insights

✅ Feature Importance Analysis

✅ Interactive Charts

✅ Clean Streamlit Dashboard
""")
    st.divider()

    st.subheader("🛠️ Technologies Used")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:
     st.markdown("""
### Programming

- Python
- Pandas
- NumPy
""")

    with tech2:
     st.markdown("""
### Machine Learning

- Scikit-learn
- Random Forest Regressor
- Joblib
""")

    with tech3:
      st.markdown("""
### Visualization

- Streamlit
- Plotly
- OpenWeather API
""")
    st.divider()

    st.subheader("📚 Dataset & Model")

    st.write("""
**Dataset**

• Indian Air Quality Dataset

• Historical records (2015–2020)

• 26 Indian Cities

• Multiple pollutant measurements

**Machine Learning Model**

• Random Forest Regressor

• Hyperparameter Tuned

• R² Score: 0.9142

• MAE: 20.23

• RMSE: 39.63
   """)
    st.divider()

    st.subheader("⚙️ AirCare AI Workflow")

    st.markdown("""
1. User selects a city.

2. OpenWeather API retrieves live AQI and pollutant data.

3. Historical pollutant data is processed by the ML model.

4. AQI prediction is generated.

5. Health advisory is displayed.

6. Interactive analytics help users understand pollution trends.
""")
    st.divider()

    st.subheader("🚀 Future Enhancements")

    st.write("""
• AQI Forecasting for the next 24–72 hours

• Interactive pollution maps

• Mobile application

• Push notifications for hazardous AQI

• Personalized user profiles

• Weather-aware AQI prediction
""")
    st.divider()

    st.success(
    "AirCare AI demonstrates an end-to-end Machine Learning workflow combining data preprocessing, predictive modeling, API integration, and interactive visualization."
)

    st.caption(
    "Developed as a Machine Learning portfolio project using Python, Scikit-learn, Streamlit, Plotly, and the OpenWeather API."
)
st.success(
    """
🎯 AirCare AI demonstrates an end-to-end Machine Learning pipeline,
combining historical data analysis, real-time API integration,
interactive visualization, and personalized health recommendations
into a single intelligent dashboard.
"""
)

    