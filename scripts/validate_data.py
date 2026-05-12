import pandas as pd
import os

# ============================================
# LOAD DATA
# ============================================

data_raw = r"C:\Users\javie\OneDrive\Documentos\supermarket-sales-dashboard\data\raw\SuperMarket Analysis.csv"
df = pd.read_csv(data_raw)

print("\nDATASET LOADED SUCCESSFULLY\n")

# ============================================
# BASIC INFO
# ============================================

print("DATASET INFO\n")
print(df.info())

# ============================================
# NUMERIC COLUMNS
# ============================================

numeric_cols = df.select_dtypes(include="number").columns

print("\nNUMERIC COLUMNS\n")
print(numeric_cols)

# ============================================
# DESCRIPTIVE STATS
# ============================================

print("\nDESCRIPTIVE STATISTICS\n")
print(df[numeric_cols].describe())

# ============================================
# NULL VALUES
# ============================================

print("\nNULL VALUES\n")
print(df[numeric_cols].isnull().sum())

# ============================================
# NEGATIVE VALUES
# ============================================

print("\nNEGATIVE VALUES CHECK\n")

for col in numeric_cols:
    negative_count = (df[col] < 0).sum()

    print(f"{col}: {negative_count}")

# ============================================
# CHECK TOTAL FORMULA
# Total ≈ cogs + tax
# ============================================

print("\nCHECKING TOTAL CONSISTENCY\n")

df["calculated_sales"] = (
    df["cogs"] + df["Tax 5%"]
)

difference = (
    df["Sales"] - df["calculated_sales"]
).abs()

invalid_rows = difference > 0.01

print(f"Inconsistent rows: {invalid_rows.sum()}")

# ============================================
# OUTLIERS CHECK (IQR)
# ============================================

print("\nOUTLIERS CHECK\n")

for col in numeric_cols:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = ((df[col] < lower) | (df[col] > upper)).sum()

    print(f"{col}: {outliers} outliers")

print("\nVALIDATION COMPLETE\n")

# ============================================
# DETAILED OUTLIERS CHECK FOR SALES
# ============================================

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers_df = df[
    (df["Sales"] < lower) |
    (df["Sales"] > upper)
]

print(outliers_df[
    [
        "Invoice ID",
        "Product line",
        "Unit price",
        "Quantity",
        "Sales"
    ]
])

# ============================================
# EXPORT CLEAN DATA
# ============================================

BASE_DIR = r"C:\Users\javie\OneDrive\Documentos\supermarket-sales-dashboard"

PROCESSED_FILE = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "clean_sales.csv"
)

df.to_csv(PROCESSED_FILE, index=False)

print("Clean dataset exported successfully.")
print(PROCESSED_FILE)