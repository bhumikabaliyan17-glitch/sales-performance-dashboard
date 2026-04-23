"""
Sales Performance Dashboard - Data Cleaning Script
Author: Bhumika Baliyan
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("SALES DATA CLEANING AND PREPARATION")
print("=" * 60)

# Create sample sales data
np.random.seed(42)
n = 10000

data = {
    'order_id': range(1, n + 1),
    'order_date': pd.date_range('2023-01-01', periods=n, freq='D'),
    'product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Printer', 'Headphones'], n),
    'category': np.random.choice(['Electronics', 'Accessories', 'Peripherals'], n),
    'region': np.random.choice(['North', 'South', 'East', 'West'], n),
    'sales': np.random.uniform(500, 50000, n),
    'quantity': np.random.randint(1, 20, n),
    'profit': np.random.uniform(50, 15000, n)
}

df = pd.DataFrame(data)

# Add calculated columns
df['profit_margin'] = (df['profit'] / df['sales']) * 100
df['year'] = pd.DatetimeIndex(df['order_date']).year
df['month'] = pd.DatetimeIndex(df['order_date']).month
df['month_name'] = pd.DatetimeIndex(df['order_date']).strftime('%B')

# Remove outliers
df = df[(df['profit_margin'] >= 0) & (df['profit_margin'] <= 100)]

print(f"\nTotal Records: {len(df):,}")
print(f"Total Sales: ₹{df['sales'].sum():,.0f}")
print(f"Total Profit: ₹{df['profit'].sum():,.0f}")
print(f"Average Profit Margin: {df['profit_margin'].mean():.1f}%")

# Save to CSV
df.to_csv('sales_data.csv', index=False)
print("\n✅ Data saved: sales_data.csv")
print("\n📊 DATA CLEANING COMPLETE!")
