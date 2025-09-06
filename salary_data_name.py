import numpy as np
import pandas as pd
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate synthetic data
years = np.random.uniform(0.5, 10, 100).round(2)  # Years of experience
salaries = (30000 + years * 6000 + np.random.normal(0, 4000, size=100)).round(2)

# Generate random names
first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey", "Jamie", "Riley", "Cameron", "Quinn", "Drew",
               "Sam", "Charlie", "Avery", "Dakota", "Reese", "Rowan", "Skyler", "Elliot", "Jesse", "Finley"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
              "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Lee", "Perez", "Thompson"]

names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(100)]

# Generate random gender
genders = [random.choice(["Male", "Female"]) for _ in range(100)]

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Gender": genders,
    "YearsExperience": years,
    "Salary": salaries
})

# Preview first few rows
print(df.head())

# Save to CSV
df.to_csv("experience_salary.csv", index=False)
print("Data saved to experience_salary.csv")
