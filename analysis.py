import pandas as pd

df = pd.read_csv("data/superstore.csv", encoding='latin1')

print(df.head())
print(df.info())
print(df.isnull().sum())
df.drop_duplicates(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month_name()
df['Year'] = df['Order Date'].dt.year
total_sales = df['Sales'].sum()
print(total_sales)
total_profit = df['Profit'].sum()
print(total_profit)
total_quantity = df['Quantity'].sum()
print(total_quantity)
category_sales = df.groupby('Category')['Sales'].sum()

print(category_sales)
category_profit = df.groupby('Category')['Profit'].sum()
monthly_sales = df.groupby('Month')['Sales'].sum()
month_order = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

monthly_sales = monthly_sales.reindex(month_order)
import plotly.express as px

fig = px.bar(
    x=category_sales.index,
    y=category_sales.values,
    title="Sales by Category"
)

fig.show()
fig = px.line(
    x=monthly_sales.index,
    y=monthly_sales.values,
    title="Monthly Sales Trend"
)

fig.show()
region_sales = df.groupby('Region')['Sales'].sum()

fig = px.pie(
    names=region_sales.index,
    values=region_sales.values,
    title="Region-wise Sales"
)

fig.show()
import sqlite3

conn = sqlite3.connect("sales.db")

df.to_sql("sales_data", conn, if_exists='replace', index=False)
query = """
SELECT Category, SUM(Sales) as TotalSales
FROM sales_data
GROUP BY Category
ORDER BY TotalSales DESC
"""

result = pd.read_sql(query, conn)

print(result)