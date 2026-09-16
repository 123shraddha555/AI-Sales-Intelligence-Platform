import pandas as pd
import mysql.connector

# Load processed data
df = pd.read_csv("data/processed/clean_sales.csv")

print("Data loaded successfully!")
print("Shape:", df.shape)


# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shraddha2410",
    database="sales_intelligence"
)

print("MySQL connection successful!")


# Insert data into MySQL
cursor = connection.cursor()

# Prepare insert query
columns = ", ".join(df.columns)
placeholders = ", ".join(["%s"] * len(df.columns))

insert_query = f"""
INSERT INTO sales ({columns})
VALUES ({placeholders})
"""

data = [tuple(row) for row in df.itertuples(index=False, name=None)]

cursor.executemany(insert_query, data)

connection.commit()

print("Data inserted successfully!")
print("Rows inserted:", cursor.rowcount)

cursor.close()
connection.close()