import streamlit as st
import pandas as pd

from utils import (
    load_data,
    load_model,
    load_city_encoder,
    load_season_encoder,
    load_feature_columns,
    prepare_input,
    get_aqi_category
)
def show_historical_prediction():
    df = load_data()

    model = load_model()

    city_encoder = load_city_encoder()

    season_encoder = load_season_encoder()

    feature_columns = load_feature_columns()
    st.title("🤖 Historical AQI Prediction")

    st.markdown("""
Predict AQI using the trained **Random Forest Regression model**
on historical air quality data (2015–2020).
""")

    st.divider()
    cities = sorted(df["City"].unique())

    city = st.selectbox(
    "🏙️ Select City",
    cities
    )
    city_df = df[df["City"] == city]

    dates = sorted(city_df["Date"].unique())

    selected_date = st.selectbox(
    "📅 Select Historical Date",
    dates
    )
    selected_row = city_df[city_df["Date"] == selected_date]

    if selected_row.empty:
      st.error("No data available.")
      return

    row = selected_row.iloc[0]
    if st.button("🤖 Predict Historical AQI"):
       historical_pollutants = {
    "pm2_5": row["PM2.5"],
    "pm10": row["PM10"],
    "no": row["NO"],
    "no2": row["NO2"],
    "nh3": row["NH3"],
    "co": row["CO"],
    "so2": row["SO2"],
    "o3": row["O3"]
}
       input_data = prepare_input(
    city,
    historical_pollutants,
    city_encoder,
    season_encoder,
    feature_columns,
    date=pd.to_datetime(selected_date)
)
       
       prediction = model.predict(input_data)[0]

       actual_aqi = row["AQI"]

       difference = abs(prediction - actual_aqi)

       category = get_aqi_category(prediction)
       st.divider()

       st.subheader("📋 Prediction Summary")

       summary_col1, summary_col2 = st.columns(2)

       with summary_col1:
        st.write(f"**🏙️ City:** {city}")
        st.write(f"**📅 Date:** {selected_date}")

       with summary_col2:
        st.write("**🤖 Model:** Random Forest Regressor")
        st.write(f"**🌿 AQI Category:** {category}")

       st.divider()

       if actual_aqi > 0:
         accuracy = max(0, 100 - (difference / actual_aqi) * 100)
       else:
         accuracy = 0

       col1, col2, col3, col4 = st.columns(4)

       with col1:
         st.metric("Predicted AQI", f"{prediction:.2f}")

       with col2:
         st.metric("Actual AQI", f"{actual_aqi:.2f}")

       with col3:
         st.metric("Prediction Error", f"{difference:.2f}")

       with col4:
          st.metric("Prediction Accuracy", f"{accuracy:.1f}%")

       if difference <= 10:
          st.success("✅ Excellent prediction. The model prediction is very close to the actual AQI.")

       elif difference <= 25:
          st.info("👍 Good prediction. The prediction is reasonably close to the actual AQI.")

       else:
          st.warning("⚠️ The prediction differs noticeably from the recorded AQI.")

       st.divider()

       st.subheader("🧪 Historical Pollutant Values")

       pollutants = {
    "PM2.5": row["PM2.5"],
    "PM10": row["PM10"],
    "NO": row["NO"],
    "NO₂": row["NO2"],
    "NOx": row["NOx"],
    "NH₃": row["NH3"],
    "CO": row["CO"],
    "SO₂": row["SO2"],
    "O₃": row["O3"],
    "Benzene": row["Benzene"],
    "Toluene": row["Toluene"],
     }

       cols = st.columns(4)

       for i, (name, value) in enumerate(pollutants.items()):
         with cols[i % 4]:
           with st.container(border=True):
            st.metric(name, f"{value:.2f}")

       st.info("""
       This prediction is generated using a Random Forest Regression model
trained on historical air quality data collected between 2015 and 2020.
The pollutant values shown above are historical observations from the dataset.
        """)
       comparison_df = pd.DataFrame({
    "Type": ["Predicted AQI", "Actual AQI"],
    "AQI": [prediction, actual_aqi]
})

       st.subheader("📈 Prediction Comparison")

       st.bar_chart(
    comparison_df.set_index("Type")
       )
       st.caption(
    "The chart compares the Random Forest model prediction against the recorded AQI value from the historical dataset."
)

       