"""
Lesson 7: Feature Engineering & Preprocessing
Concepts: Handling Nulls, Scaling, Encoding.
Why? Raw data is usually messy. ML model algorithms (like SVM/KNN) fail without scaling.
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. Handling Missing Data
data = {
    'Price': [200, 250, np.nan, 300, 350],
    'Category': ['A', 'B', 'A', np.nan, 'B'],
    'Value': [10, 15, 20, 25, 30]
}
df = pd.DataFrame(data)

print("--- Data with Missing Values ---")
print(df)

# Fill numeric with mean, categorical with mode
df['Price'] = df['Price'].fillna(df['Price'].mean())
df['Category'] = df['Category'].fillna(df['Category'].mode()[0])
print("\n--- Cleaned Data ---")
print(df)

# 2. Encoding (Converting Text to Numbers)
# ML models can't read 'A' or 'B'
le = LabelEncoder()
df['Category_Encoded'] = le.fit_transform(df['Category'])
print("\n--- After Label Encoding ---")
print(df)

# 3. Scaling (Scaling values to a similar range)
# 'Value' is 10-30, 'Price' is 100s. We need them on the same scale.
scaler = StandardScaler()
df[['Price', 'Value']] = scaler.fit_transform(df[['Price', 'Value']])
print("\n--- After Standard Scaling (Z-Score) ---")
print(df)

print("\n--- ML Tip ---")
print("Always PREPROCESS before TRAINING. Scaling often makes the difference between 50% and 90% accuracy.")
