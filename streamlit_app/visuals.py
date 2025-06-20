# streamlit_app/visuals.py
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_graphs(df):
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Area vs Price")
        fig1, ax1 = plt.subplots()
        sns.scatterplot(x="area", y="price", data=df, ax=ax1)
        ax1.set_xlabel("Area (sq. ft)")
        ax1.set_ylabel("Price (Lakhs)")
        st.pyplot(fig1)

    with col2:
        st.write("### BHK vs Price")
        fig2, ax2 = plt.subplots()
        sns.boxplot(x="bhk", y="price", data=df, ax=ax2)
        ax2.set_xlabel("BHK")
        ax2.set_ylabel("Price (Lakhs)")
        st.pyplot(fig2)
