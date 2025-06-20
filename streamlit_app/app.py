import streamlit as st
import pandas as pd
import pickle
from visuals import show_graphs
from inputs import get_user_input

# Load trained model
model = pickle.load(open("house_price_model.pkl", "rb"))

# Load housing dataset for visualization
df = pd.read_csv("housing_data.csv")

st.set_page_config(page_title="House Price Predictor", layout="wide")
st.title("🏠 House Price Prediction System")

# Sidebar input
user_input_df = get_user_input()

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(user_input_df)[0]
    st.success(f"💰 Predicted House Price: ₹{round(prediction, 2)} Lakhs")

# Graphs
st.subheader("📈 Visual Analysis")
show_graphs(df)
