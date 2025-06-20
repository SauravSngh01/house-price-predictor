# streamlit_app/app.py
import streamlit as st
import pandas as pd
import pickle
from visuals import show_graphs
from inputs import get_user_input

# Load model
model = pickle.load(open("../model/house_price_model.pkl", "rb"))

# Load housing data for visualizations
df = pd.read_csv("../data/housing_data.csv")

st.set_page_config(page_title="House Price Predictor", layout="wide")
st.title("🏠 House Price Prediction System")

# Get user input
user_input_df = get_user_input()

# Predict
if st.button("Predict Price"):
    prediction = model.predict(user_input_df)[0]
    st.success(f"💰 Predicted House Price: ₹{round(prediction, 2)} Lakhs")

# Show visualizations
st.subheader("📈 Visual Analysis")
show_graphs(df)
