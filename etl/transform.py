import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw/superstore_sales.csv", encoding="cp1252")
print("Original Shape:")
print(df.shape)
print("\nOriginal Data Types:")
print(df.dtypes)


# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("\nCleaned Column Names:")
print(df.columns)

# Fix sub-category column name
df.rename(columns={"sub-category": "sub_category"}, inplace=True)
print("\nFinal Column Names:")
print(df.columns)


# Convert date columns to datetime
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])
print("\nDate Data Types:")
print(df[["order_date", "ship_date"]].dtypes)


# Check missing values after transformation
print("\nMissing Values:")
print(df.isnull().sum())


# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())


# Check minimum values of numerical columns
print("\nMinimum Values:")
print(df[["sales", "quantity", "discount", "profit"]].min())


# Check maximum values of numerical columns
print("\nMaximum Values:")
print(df[["sales", "quantity", "discount", "profit"]].max())


# Create date-based columns
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df["order_quarter"] = df["order_date"].dt.quarter
print("\nNew Date Columns:")
print(df[["order_date", "order_year", "order_month", "order_quarter"]].head())

# Calculate shipping days
df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days
print("\nShipping Days:")
print(df[["order_date", "ship_date", "shipping_days"]].head())


# Check shipping days
print("\nShipping Days Statistics:")
print(df["shipping_days"].describe())
print("\nMinimum Shipping Days:")
print(df["shipping_days"].min())


# Save transformed data
df.to_csv("data/processed/clean_sales.csv", index=False)
print("\nCleaned data saved successfully!")


# Verify processed data
processed_df = pd.read_csv("data/processed/clean_sales.csv")
print("\nProcessed Data Shape:")
print(processed_df.shape)
print("\nProcessed Data Preview:")
print(processed_df.head())