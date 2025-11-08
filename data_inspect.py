import pandas as pd

# Path to your dataset (change this as needed)
file_path = "Super Store Sales/SuperStoreUS-2015.xlsx"

# Read Excel file
df = pd.read_excel(file_path)

# Summary statistics
print("\nSummary Statistics:")
#print(df.describe(include='all').T)
print(df.groupby('Region')['Sales'].sum())
print(df['Customer Name'].value_counts().head())

