import pandas as pd

# Path to your dataset (change this as needed)
file_path = "Super Store Sales/SuperStoreUS-2015.xlsx"

# Read Excel file
df = pd.read_excel(file_path)


# Summary statistics
print("\n📊 Summary Statistics:")
print(df.describe(include='all').T)


