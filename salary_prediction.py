import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

st.title("Salary Prediction using Linear Regression")

# Option to upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Using default generated data")
    import numpy as np
    np.random.seed(42)
    years = np.random.uniform(0.5, 10, 100).round(2)
    salaries = (30000 + years * 6000 + np.random.normal(0, 4000, size=100)).round(2)
    df = pd.DataFrame({
        "YearsExperience": years,
        "Salary": salaries
    })

st.subheader("Dataset")
st.dataframe(df.head(10))

# Features and target
X = df[["YearsExperience"]]
y = df["Salary"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

st.subheader("Model Metrics")
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
st.write(f"**Mean Squared Error:** {mse:.2f}")
st.write(f"**R² Score:** {r2:.2f}")
st.write(f"**Model Coefficient (Slope):** {model.coef_[0]:.2f}")
st.write(f"**Model Intercept:** {model.intercept_:.2f}")

# Prediction input
st.subheader("Predict Salary")
years_input = st.number_input("Enter Years of Experience", min_value=0.0, max_value=50.0, value=1.0, step=0.1)
predicted_salary = model.predict([[years_input]])[0]
st.success(f"Predicted Salary: ${predicted_salary:.2f}")

# Plot
st.subheader("Salary vs Years of Experience")
fig, ax = plt.subplots()
ax.scatter(X, y, color='blue', label='Actual Salary')
ax.plot(X, model.predict(X), color='red', linewidth=2, label='Predicted Salary')
ax.set_xlabel("Years of Experience")
ax.set_ylabel("Salary")
ax.legend()
st.pyplot(fig)
