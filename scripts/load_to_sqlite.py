import pandas as pd
import sqlite3
import os

# ============================================
# BASE PATH
# ============================================

BASE_DIR = r"C:\Users\javie\OneDrive\Documentos\supermarket-sales-dashboard"

# ============================================
# FILE PATHS
# ============================================

CSV_FILE = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "clean_sales.csv"
)

DB_FILE = os.path.join(
    BASE_DIR,
    "database",
    "sales.db"
)

# Create database folder
os.makedirs(
    os.path.join(BASE_DIR, "database"),
    exist_ok=True
)

# ============================================
# LOAD CSV
# ============================================

df = pd.read_csv(CSV_FILE)

# ============================================
# CONNECT SQLITE
# ============================================

conn = sqlite3.connect(DB_FILE)

# ============================================
# EXPORT TABLE
# ============================================

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

print("Data loaded into SQLite successfully.")

# ============================================
# CLOSE CONNECTION
# ============================================

conn.close()