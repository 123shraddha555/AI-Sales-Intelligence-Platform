
from google import genai
import os
import mysql.connector

# -----------------------------
# 1. Create Gemini client
# -----------------------------

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -----------------------------
# 2. User question
# -----------------------------

question = input("Enter your question: ")
# -----------------------------
# 3. Ask Gemini to generate SQL
# -----------------------------

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"""
You are a SQL expert.

Database:
MySQL

Table:
sales

Columns:
category
sales
profit
order_date
region
product_name
customer_name

Convert the following question into a MySQL SQL query.

Question:
{question}

Return only the SQL query.
Do not use markdown.
Do not add explanations.
"""
)

sql_query = response.text.strip()

print("\nGenerated SQL:")
print(sql_query)


# -----------------------------
# 3.5 SQL Safety Validation
# -----------------------------

if not sql_query.lower().startswith("select"):
    print("\nUnsafe SQL query detected!")
    exit()

print("\nSQL query is safe to execute.")

# -----------------------------
# 4. Connect to MySQL
# -----------------------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shraddha2410",
    database="sales_intelligence"
)

cursor = connection.cursor()

print("\nMySQL connection successful!")

# -----------------------------
# 5. Execute generated SQL
# -----------------------------

cursor.execute(sql_query)

result = cursor.fetchall()

print("\nMySQL Result:")

if result:
    for row in result:
        print(row)
else:
    print("No result found.")


print("\nNatural Language Answer:")

if result:
    result_text = str(result)

    answer_response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
Convert the following SQL result into a simple natural language answer.

User question:
{question}

SQL result:
{result_text}

Give only the answer.
Do not mention SQL.
Do not use technical terms.
"""
    )

    print("Answer:", answer_response.text.strip())

else:
    print("No result found.")
# -----------------------------

# 6. Close connection
# -----------------------------

cursor.close()
connection.close()

print("\nConnection closed.")