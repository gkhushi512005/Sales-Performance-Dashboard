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