import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Transaction Visualizer", layout="centered")

st.title("📊 Customer Transactions Dashboard")
st.write("Upload your transaction CSV file and explore your data!")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    try:
        # Load the file
        df = pd.read_csv(uploaded_file)

        # Show raw data
        st.subheader("🔍 Raw Data")
        st.write(df.head())

        # Drop rows with missing values
        df_clean = df.dropna()

        # Try to find the 'Amount' column (case-insensitive)
        amount_column = None
        for col in df_clean.columns:
            if "amount" in col.lower():
                amount_column = col
                break

        if amount_column:
            # Convert to numeric, drop non-numeric rows
            df_clean[amount_column] = pd.to_numeric(df_clean[amount_column], errors="coerce")
            df_clean = df_clean.dropna(subset=[amount_column])

            st.subheader("🧼 Cleaned Data")
            st.write(df_clean.head())

            st.subheader("📈 Amount Distribution")
            fig, ax = plt.subplots()
            ax.hist(df_clean[amount_column], bins=20, color="#4CAF50", edgecolor="black")
            ax.set_xlabel("Amount")
            ax.set_ylabel("Frequency")
            ax.set_title("Histogram of Transaction Amounts")
            st.pyplot(fig)

        else:
            st.warning("No column with name like 'Amount' found. Please check your file.")

    except Exception as e:
        st.error(f"Something went wrong while processing your file: {e}")
else:
    st.info("👆 Please upload a CSV file to get started.")
