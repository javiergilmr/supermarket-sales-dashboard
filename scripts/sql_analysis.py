import sqlite3
import pandas as pd
import os

BASE_DIR = r"C:\Users\javie\OneDrive\Documentos\supermarket-sales-dashboard"

DB_FILE = os.path.join(
    BASE_DIR,
    "database",
    "sales.db"
)

conn = sqlite3.connect(DB_FILE)

query = """
SELECT
    city,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales
GROUP BY city
ORDER BY total_sales DESC
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()