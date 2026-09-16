from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from xgboost import XGBRegressor
import pandas as pd

# Load processed sales data
df = pd.read_csv("data/processed/clean_sales.csv")

print("Data loaded successfully!")
print("Shape:", df.shape)

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Create monthly sales
monthly_sales = (
    df.assign(
        year=df["order_date"].dt.year,
        month=df["order_date"].dt.month
    )
    .groupby(["year", "month"])["sales"]
    .sum()
    .reset_index()
)

# Create date column
monthly_sales["date"] = pd.to_datetime(
    monthly_sales[["year", "month"]].assign(day=1)
)

# Sort by date
monthly_sales = monthly_sales.sort_values("date")

print("\nMonthly Sales with Date:")
print(monthly_sales.head(10))

# Create ML features
monthly_sales["month_number"] = range(1, len(monthly_sales) + 1)

# Previous month's sales
monthly_sales["previous_month_sales"] = monthly_sales["sales"].shift(1)

print("\nML Features:")
print(monthly_sales.head(10))

# Remove first row because it has no previous month sales
monthly_sales = monthly_sales.dropna().reset_index(drop=True)

print("\nFinal Shape:")
print(monthly_sales.shape)

# Define features and target
X = monthly_sales[
    [
        "year",
        "month",
        "month_number",
        "previous_month_sales"
    ]
]

y = monthly_sales["sales"]

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

# Split data into training and testing sets
train_size = int(len(X) * 0.8)

X_train = X.iloc[:train_size]
X_test = X.iloc[train_size:]

y_train = y.iloc[:train_size]
y_test = y.iloc[train_size:]

print("\nTraining Data:")
print("X_train:", X_train.shape)
print("y_train:", y_train.shape)

print("\nTesting Data:")
print("X_test:", X_test.shape)
print("y_test:", y_test.shape)

# Create XGBoost model
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.05,
    max_depth=3,
    random_state=42
)

print("\nXGBoost model created successfully!")

# Train the model
model.fit(X_train, y_train)

print("\nXGBoost model trained successfully!")

# Make predictions
predictions = model.predict(X_test)

print("\nPredictions:")
print(predictions)

# Compare actual and predicted sales
comparison = pd.DataFrame({
    "Actual_Sales": y_test.values,
    "Predicted_Sales": predictions
})

print("\nActual vs Predicted Sales:")
print(comparison)

# Calculate MAE
mae = mean_absolute_error(y_test, predictions)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("\nModel Evaluation:")
print("MAE:", mae)
print("RMSE:", rmse)

# Save forecasting results
forecast_results = monthly_sales.iloc[train_size:].copy()

forecast_results["actual_sales"] = y_test.values
forecast_results["predicted_sales"] = predictions

forecast_results.to_csv(
    "data/processed/sales_forecast.csv",
    index=False
)

print("\nForecast results saved successfully!")