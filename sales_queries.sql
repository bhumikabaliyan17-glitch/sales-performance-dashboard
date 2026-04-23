-- Sales Performance Dashboard - SQL Analysis
-- Author: Bhumika Baliyan

-- 1. Total Sales by Region
SELECT region, 
       ROUND(SUM(sales), 0) as total_sales,
       ROUND(SUM(profit), 0) as total_profit
FROM sales_data
GROUP BY region
ORDER BY total_sales DESC;

-- 2. Top 5 Products by Sales
SELECT product, 
       ROUND(SUM(sales), 0) as total_sales
FROM sales_data
GROUP BY product
ORDER BY total_sales DESC
LIMIT 5;

-- 3. Monthly Sales Trend
SELECT month_name,
       ROUND(SUM(sales), 0) as total_sales
FROM sales_data
GROUP BY month_name
ORDER BY total_sales DESC;

-- 4. Profit by Category
SELECT category,
       ROUND(SUM(profit), 0) as total_profit,
       ROUND(AVG(profit_margin), 2) as avg_margin
FROM sales_data
GROUP BY category
ORDER BY total_profit DESC;
