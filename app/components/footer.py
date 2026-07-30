import streamlit as st

def show_footer():
    st.divider()

    col1, col2 = st.columns([3, 1])

    with col1:
        st.caption(
            "🌿 AirCare AI | Built with Streamlit • Scikit-learn • OpenWeather API"
        )

    with col2:
        st.caption("Version 1.0")