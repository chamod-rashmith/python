"""
Exercise: Feature Engineering & Preprocessing
Goal: Transform a raw dataset into a 'Model-Ready' format.
"""
import pandas as pd
import numpy as np

# 1. Raw Data
raw_data = {
    'Weight': [150, 160, np.nan, 180, 200, 155],
    'City': ['NY', 'NY', 'LA', 'LA', 'SF', 'SF'],
    'Price': [10, 12, 15, 11, 20, 18]
}
df = pd.DataFrame(raw_data)

# Task 1: Fill the missing 'Weight' with the mean value.

# Task 2: Use One-Hot Encoding (pd.get_dummies) to convert 'City' into numeric columns.

# Task 3: Use StandardScaler to scale 'Weight' and 'Price'.

# Task 4: Print the final DataFrame. It should have no text and all values should be scaled.

print("--- Feature Engineering Challenge ---")
# Start coding here...
