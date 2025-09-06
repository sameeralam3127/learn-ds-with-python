import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
years = np.random.uniform(0.5, 10, 100).round(2)  # Years of experience
salaries = (30000 + years * 6000 + np.random.normal(0, 4000, size=100)).round(2)

# Create DataFrame
df = pd.DataFrame({
    "YearsExperience": years,
    "Salary": salaries
})

# Preview first few rows
print(df.head())

# Save to CSV
df.to_csv("experience_salary.csv", index=False)
print("Data saved to experience_salary.csv")
