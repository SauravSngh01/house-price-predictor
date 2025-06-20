# streamlit_app/inputs.py
import streamlit as st
import pandas as pd

def get_user_input():
    area = st.slider("📐 Area (sq. ft)", 300, 5000, 1000)
    bhk = st.selectbox("🛏️ BHK", [1, 2, 3, 4, 5])
    location = st.selectbox("📍 Location", ["Mumbai", "Delhi", "Bangalore"])

    input_dict = {
        "area": area,
        "bhk": bhk,
        "location_Bangalore": 1 if location == "Bangalore" else 0,
        "location_Delhi": 1 if location == "Delhi" else 0,
        "location_Mumbai": 1 if location == "Mumbai" else 0
    }

    return pd.DataFrame([input_dict])
