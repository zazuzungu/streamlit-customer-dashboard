import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("📊 Customer Transactions Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Read data
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Raw Data")
    st.dataframe(df.head())

    # Basic Cleaning
    st.subheader("🧼 Cleaned Data Summary")
    st.write("We’ll drop rows with missing values and ensure correct datatypes.")

    df_clean = df.dropna()
    st.dataframe(df_clean.describe())

    # Basic Visualization
    st.subheader("📈 Transaction Amounts Histogram")

    if "Amount" in df_clean.columns:
        fig, ax = plt.subplots()
        ax.hist(df_clean["Amount"], bins=20, color="#4CAF50", edgecolor="black")
        ax.set
