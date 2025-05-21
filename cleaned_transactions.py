import pandas as pd

# Load the uploaded csv
df = pd.read_csv("transactions.csv")

# Preview the data
df.head()

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Check for duplicates
print("\nDuplicate rows:", df.duplicated().sum())

# Check data types
print("\nData types:\n", df.dtypes)

# Extra steps as additional measures to ensure code is spotless
# Drop duplicates if any
df.drop_duplicates(inplace=True)

# Convert transaction_date to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Trim whitespace in string columns (in case of inconsistent entries)

for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

df.head()

# We are now moving on to transforming this squeaky clean data
# Let the data speak. We are finding the total amount spent per customer

total_per_customer = df.groupby("customer_id")["amount"].sum().reset_index()
total_per_customer.rename(columns = {"amount": "total_amount"}, inplace=True)
total_per_customer

# Finding the most popular product
most_popular_product = df["product"].value_counts().idxmax()
print("Most popular product:", most_popular_product)

# Finding the total amount per region
total_by_region = df.groupby("region")["amount"].sum().reset_index()
total_by_region.sort_values(by = "amount", ascending = False)

import sqlite3

# Creating an in-memory SQLite database
conn = sqlite3.connect(':memory:')

# Loading DataFrame into SQL as a table
df.to_sql('transactions', conn, index=False, if_exists='replace')

# Querying for total amount per region 
query = """
SELECT region, SUM(amount) AS total_amount
FROM transactions
GROUP BY region
ORDER BY total_amount DESC
"""
pd.read_sql_query(query, conn)

# Finding transactions for a specific customer
query = """
SELECT *
FROM transactions
WHERE customer_id = 'CUST001'
"""
pd.read_sql_query(query, conn)

# Counting of transactions per product
query = """
SELECT product, COUNT(*) as num_transactions
FROM transactions
GROUP BY product
ORDER BY num_transactions DESC
"""
pd.read_sql_query(query, conn)

# Combining conditions
query = """
SELECT *
FROM transactions
WHERE region = 'Gauteng' AND amount > 500
"""
pd.read_sql_query(query, conn)
