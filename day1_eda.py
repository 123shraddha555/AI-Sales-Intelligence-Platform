import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/superstore_sales.csv", encoding="cp1252")
# First 5 rows
print("First 5 rows:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())


# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
print(category_sales)


# Sales and Profit by Region
region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum()
print("\nSales and Profit by Region:")
print(region_analysis)

# Sales by Sub-Category
subcategory_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Sub-Category:")
print(subcategory_sales)

# Profit by Sub-Category
subcategory_profit = df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False)

print("\nProfit by Sub-Category:")
print(subcategory_profit)

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Sales and Profit by Year
yearly_analysis = df.groupby(df["Order Date"].dt.year)[["Sales", "Profit"]].sum()

print("\nSales and Profit by Year:")
print(yearly_analysis)