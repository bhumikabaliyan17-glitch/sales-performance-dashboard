# 📊 Sales Performance Dashboard

> An end-to-end data analytics project demonstrating proficiency in **Python**, **SQL**, and **Power BI**

---

## 📌 Project Overview

This project simulates a real-world business scenario where a retail company needs to analyze its sales performance. The goal was to clean raw sales data, perform exploratory analysis, extract insights using SQL, and present them through an interactive dashboard.

**Complete workflow:** `Data Cleaning (Python)` → `Querying (SQL)` → `Visualization (Power BI)`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | Data cleaning, transformation, statistical analysis |
| <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | Data extraction, aggregation, complex queries |
| <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"> | Interactive dashboard, visual storytelling |
| <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"> | Version control, portfolio hosting |

---

## 📂 Dataset Description

- **Source:** Simulated retail sales data (10,000+ records)
- **Time Period:** 12 months
- **Key Columns:** Order Date, Product, Category, Region, Sales, Profit, Quantity

| Column | Description |
|--------|-------------|
| `order_id` | Unique transaction ID |
| `order_date` | Date of purchase |
| `product_name` | Product purchased |
| `category` | Product category (Electronics/Accessories/Peripherals) |
| `region` | Sales region (North/South/East/West) |
| `sales` | Revenue generated (₹) |
| `profit` | Profit earned (₹) |
| `quantity` | Number of units sold |

---

## 🔧 Data Cleaning (Python)

### Steps Performed:

| # | Task | Tool/Method |
|---|------|-------------|
| 1 | Load CSV data | `pandas.read_csv()` |
| 2 | Handle missing values | `fillna()` with median |
| 3 | Remove duplicates | `drop_duplicates()` |
| 4 | Add calculated columns | Profit Margin = Profit/Sales * 100 |
| 5 | Remove outliers | Filter profit margin 0-100% |
| 6 | Export cleaned data | CSV + SQLite database |

### Sample Code:
```python
# Load and clean data
df = pd.read_csv('sales_data.csv')
df['profit_margin'] = (df['profit'] / df['sales']) * 100
df = df[(df['profit_margin'] >= 0) & (df['profit_margin'] <= 100)]
