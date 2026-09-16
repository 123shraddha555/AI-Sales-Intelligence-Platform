# AI-Powered Sales Intelligence Platform

An AI-powered sales analytics and data engineering platform built using Python, SQL, MySQL, Machine Learning, Gemini AI, and Power BI.

The project processes raw sales data, cleans and transforms it, stores it in MySQL, performs SQL analytics, generates sales forecasts and detects anomalies using Machine Learning, and allows users to ask questions about sales data using natural language.

## Project Workflow

Raw Sales Data
↓
Data Ingestion
↓
Data Cleaning & Transformation using Python
↓
MySQL Database
↓
SQL Analytics
↓
Machine Learning
├── Sales Forecasting
└── Anomaly Detection
↓
Gemini AI Text-to-SQL
↓
Power BI Dashboard

## Technologies Used

- Python
- Pandas
- NumPy
- MySQL
- SQL
- Scikit-learn
- XGBoost
- Gemini AI
- Power BI
- Git & GitHub

## Key Features

- Data ingestion and preprocessing using Python and Pandas
- Data cleaning and transformation through an ETL pipeline
- MySQL database for storing processed sales data
- SQL queries for sales and profit analysis
- XGBoost-based sales forecasting
- Isolation Forest-based anomaly detection
- Gemini AI-based natural language to SQL conversion
- Natural language answers generated from database results
- Interactive Power BI dashboard for sales insights

## Machine Learning

### Sales Forecasting

XGBoost Regressor is used to forecast monthly sales based on historical sales patterns and previous-month sales.

Evaluation metrics:
- Mean Absolute Error (MAE): 17,270.45
- Root Mean Squared Error (RMSE): 20,465.21

### Anomaly Detection

Isolation Forest is used to identify unusual sales records based on:

- Sales
- Quantity
- Discount
- Profit

Anomaly records are marked with `-1`, while normal records are marked with `1`.

## Gemini AI — Natural Language to SQL

The project uses Gemini AI to convert natural language questions into MySQL queries.

Example:

```text
User Question
      ↓
Gemini AI
      ↓
SQL Query
      ↓
Safety Validation
      ↓
MySQL Database
      ↓
Query Result
      ↓
Gemini AI
      ↓
Natural Language Answer

## Power BI Dashboard

The interactive Power BI dashboard provides:

- Total Sales KPI
- Total Profit KPI
- Total Orders KPI
- Profit Margin KPI
- Monthly Sales Trend
- Sales by Category
- Sales by Region
- Profit by Category
- Actual vs Predicted Sales
- Anomaly Detection visualization
- Region and Category filters

The dashboard connects to the MySQL sales database and the machine learning output files.


## Project Structure

```text
AI-Sales-Intelligence-Platform/
│
├── ai/
│   └── text_to_sql.py
│
├── data/
│   ├── raw/
│   │   └── superstore_sales.csv
│   └── processed/
│       ├── clean_sales.csv
│       ├── sales_anomalies.csv
│       └── sales_forecast.csv
│
├── data_quality/
│   └── validation.py
│
├── etl/
│   ├── transform.py
│   └── load.py
│
├── ml/
│   ├── forecasting.py
│   └── anomaly_detection.py
│
├── sql/
│   └── sales.sql
│
├── day1_eda.py
├── requirements.txt
├── .gitignore
└── README.md


## Setup and Usage

### 1. Clone the repository

```bash
git clone https://github.com/123shraddha555/AI-Sales-Intelligence-Platform.git
cd AI-Sales-Intelligence-Platform


