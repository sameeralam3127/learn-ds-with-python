import pandas as pd

# Path to your dataset (change this as needed)
file_path = "Super Store Sales/SuperStoreUS-2015.xlsx"

# Read Excel file
df = pd.read_excel(file_path)

print("="*60)
print(f"📂 Loaded Dataset: {file_path}")
print(f"✅ Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print("="*60)

# Column info
print("\n🧾 Basic Info:")
print(df.info())

# Summary statistics
print("\n📊 Summary Statistics:")
print(df.describe(include='all').T)

# Missing values
print("\n⚠️ Missing Values:")
print(df.isna().sum()[df.isna().sum() > 0])

# Sample data
print("\n🔍 Sample Rows:")
print(df.head(10))

print("\n✅ Inspection complete.")
