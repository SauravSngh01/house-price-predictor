import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_graphs(df):
    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots()
        sns.scatterplot(data=df, x="area", y="price", hue="location", ax=ax1)
        plt.title("Area vs Price")
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots()
        sns.boxplot(data=df, x="bhk", y="price", ax=ax2)
        plt.title("BHK vs Price")
        st.pyplot(fig2)

