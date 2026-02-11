"""
Lesson 5: Pandas Basics
Pandas is build on NumPy and provides DataFrames (like Excel tables).
It is the standard tool for data manipulation in Python.
"""
import pandas as pd
import numpy as np

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'Chicago', 'Houston'],
    'Salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)

print("--- Full DataFrame ---")
print(df)

print("\n--- Selecting Data ---")
print(f"Only Ages:\n{df['Age']}")

print("\n--- Filtering Data ---")
print("People older than 30:")
print(df[df['Age'] > 30])

print("\n--- Basic Statistics ---")
print(df.describe())

# Adding a column
df['Junior'] = df['Age'] < 30
print("\n--- Modified DataFrame ---")
print(df)

print("\n--- ML Context ---")
print("You will use Pandas to load CSV files and clean 'missing values' before feeding data to your ML model.")
