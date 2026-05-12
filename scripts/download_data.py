import os
import shutil
from dotenv import load_dotenv
import kagglehub

# ============================================
# LOAD ENV
# ============================================

load_dotenv()

os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")

# ============================================
# DOWNLOAD DATASET
# ============================================

path = kagglehub.dataset_download(
    "faresashraf1001/supermarket-sales"
)

print(f"Dataset downloaded at:\n{path}")

# ============================================
# LIST FILES
# ============================================

files = os.listdir(path)

print("\nFiles found:")
for file in files:
    print(f"- {file}")

# ============================================
# PROJECT ROOT
# ============================================

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")

os.makedirs(RAW_DIR, exist_ok=True)

# ============================================
# FIND CSV
# ============================================

csv_file = None

for file in files:
    if file.endswith(".csv"):
        csv_file = file
        break

if not csv_file:
    raise FileNotFoundError("No CSV file found.")

# ============================================
# COPY CSV
# ============================================

source_file = os.path.join(path, csv_file)

destination_file = os.path.join(
    RAW_DIR,
    csv_file
)

shutil.copy(source_file, destination_file)

print("\nCSV copied successfully:")
print(destination_file)