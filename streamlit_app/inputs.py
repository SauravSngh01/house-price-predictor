import streamlit as st
import pandas as pd

def get_user_input():
    st.sidebar.header("Enter House Details")

    area = st.sidebar.slider("Area (in sq. ft)", 500, 5000, 1500)
    bhk = st.sidebar.selectbox("BHK", [1, 2, 3, 4, 5])
    location = st.sidebar.selectbox("Location", [
        'Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Chennai', 
        'Kolkata', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow'
    ])

    # One-hot encode location
    loc_dict = {
        'Delhi': 0, 'Mumbai': 0, 'Bangalore': 0, 'Hyderabad': 0,
        'Chennai': 0, 'Kolkata': 0, 'Pune': 0, 'Ahmedabad': 0,
        'Jaipur': 0, 'Lucknow': 0
    }
    loc_dict[location] = 1

    input_data = {
        'area': [area],
        'bhk': [bhk],
        **{f'loc_{k}': [v] for k, v in loc_dict.items()}
    }

    return pd.DataFrame(input_data)

