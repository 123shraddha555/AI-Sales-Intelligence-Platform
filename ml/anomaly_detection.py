import pandas as pd
from sklearn.ensemble import IsolationForest

# Load processed sales data
df = pd.read_csv("data/processed/clean_sales.csv")

print("Data loaded successfully!")
print("Shape:", df.shape)

# Select multiple features
X = df[
    [
        "sales",
        "quantity",
        "discount",
        "profit"
    ]
]

print("\nSelected features:")
print(X.head())

# Create Isolation Forest model
model = IsolationForest(
    contamination=0.05,
    random_state=42
)

# Train the model
model.fit(X)

print("\nIsolation Forest model trained successfully!")

# Predict anomalies
df["anomaly"] = model.predict(X)

print("\nAnomaly Results:")
print(
    df[
        [
            "order_id",
            "sales",
            "quantity",
            "discount",
            "profit",
            "anomaly"
        ]
    ].head(20)
)


# Save anomaly results
df.to_csv(
    "data/processed/sales_anomalies.csv",
    index=False
)

print("\nAnomaly results saved successfully!")