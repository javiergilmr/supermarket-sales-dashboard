import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================================
# BASE PATH
# ============================================

BASE_DIR = r"C:\Users\javie\OneDrive\Documentos\supermarket-sales-dashboard"

# ============================================
# FILE PATH
# ============================================

FILE_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "clean_sales.csv"
)

# ============================================
# LOAD DATA
# ============================================

df = pd.read_csv(FILE_PATH)

print(df.columns)

print(df["City"].unique())

print("\nDATASET LOADED SUCCESSFULLY\n")

# ============================================
# BASIC INFO
# ============================================

print(df.head())

print("\nDATASET SHAPE\n")
print(df.shape)

# ============================================
# SALES BY PRODUCT LINE
# ============================================

sales_by_product = (
    df.groupby("Product line")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSALES BY PRODUCT LINE\n")
print(sales_by_product)

plt.figure(figsize=(10, 6))

sales_by_product.plot(kind="bar")

plt.title("Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# ============================================
# SALES BY CITY
# ============================================

sales_by_city = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSALES BY CITY\n")
print(sales_by_city)

plt.figure(figsize=(8, 5))

sales_by_city.plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.show()

# ============================================
# SALES BY PAYMENT METHOD
# ============================================

sales_by_payment = (
    df.groupby("Payment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSALES BY PAYMENT METHOD\n")
print(sales_by_payment)

plt.figure(figsize=(8, 5))

sales_by_payment.plot(kind="bar")

plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.show()

# ============================================
# SALES BY HOUR
# ============================================

df["hour"] = pd.to_datetime(df["Date"]).dt.hour
sales_by_hour = (
    df.groupby("hour")["Sales"]
    .sum()
)

print("\nSALES BY HOUR\n")
print(sales_by_hour)

plt.figure(figsize=(10, 5))

sales_by_hour.plot(kind="line", marker="o")

plt.title("Sales by Hour")
plt.xlabel("Hour")
plt.ylabel("Total Sales")

plt.grid(True)

plt.tight_layout()

plt.show()

# ============================================
# PROFIT BY CITY
# ============================================

profit_by_city = (
    df.groupby("City")["gross income"]
    .sum()
    .sort_values(ascending=False)
)

print("\nPROFIT BY CITY\n")
print(profit_by_city)

plt.figure(figsize=(8, 5))

profit_by_city.plot(kind="bar")

plt.title("Profit by City")
plt.xlabel("City")
plt.ylabel("Profit")

plt.tight_layout()

plt.show()

# ============================================
# CORRELATION
# ============================================

correlation = df[["Rating", "Sales"]].corr()

print("\nCORRELATION BETWEEN RATING AND SALES\n")
print(correlation)

# ============================================
# TOP 10 SALES
# ============================================

top_sales = df.sort_values(
    by="Sales",
    ascending=False
).head(10)

print("\nTOP 10 SALES\n")
print(
    top_sales[
        [
            "Invoice ID",
            "City",
            "Product line",
            "Sales"
        ]
    ]
)

print("\nEDA COMPLETE\n")