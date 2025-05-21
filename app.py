import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Customer Data Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload your cleaned CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Preview of Data")
    st.write(df.head())

    # Summary Stats
    st.subheader("Summary Statistics")
    st.write(df.describe(include='all'))

    # Bar Chart Example: Customers by Gender (change column if needed)
    if 'gender' in df.columns:
        st.subheader("Gender Distribution")
        gender_counts = df['gender'].value_counts()
        st.bar_chart(gender_counts)

    # Pie Chart Example: Customer Country Distribution
    if 'country' in df.columns:
        st.subheader("Customers by Country")
        country_counts = df['country'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(country_counts, labels=country_counts.index, autopct="%1.1f%%")
        ax.axis("equal")
        st.pyplot(fig)
