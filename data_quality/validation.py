import pandas as pd

# Load processed data
df = pd.read_csv("data/processed/clean_sales.csv")

print("Data loaded successfully!")
print("Shape:", df.shape)

# 1. Check missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 2. Check duplicate rows
print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

# 3. Check invalid sales values
print("\n--- Invalid Sales Values ---")
print((df["sales"] < 0).sum())

# 4. Check invalid quantity values
print("\n--- Invalid Quantity Values ---")
print((df["quantity"] <= 0).sum())

# 5. Check invalid discount values
print("\n--- Invalid Discount Values ---")
print(((df["discount"] < 0) | (df["discount"] > 1)).sum())

# 6. Check invalid shipping days
print("\n--- Invalid Shipping Days ---")
print((df["shipping_days"] < 0).sum())

print("\nData quality validation completed!")