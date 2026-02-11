"""
Exercise: The Titanic Challenge (Simplified)
Goal: Predict if a passenger survived based on their data.
This combines Pandas, Preprocessing, and Machine Learning.
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# 1. Dummy Titanic Data (Normally you'd load a CSV)
raw_data = {
    'Pclass': [3, 1, 3, 1, 3, 1, 3, 2],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female'],
    'Age': [22, 38, 26, 35, 35, np.nan, 54, 2],
    'Fare': [7.25, 71.28, 7.92, 53.10, 8.05, 8.45, 51.86, 21.07],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 1]
}

df = pd.DataFrame(raw_data)

# --- YOUR TASKS ---

# Task 1: Handle the missing 'Age' (Fill with the median)
# df['Age'] = ...

# Task 2: Encode 'Sex' into numbers (male=1, female=0)
# le = LabelEncoder()
# df['Sex'] = ...

# Task 3: Separate Features (Pclass, Sex, Age, Fare) from Target (Survived)
# X = ...
# y = ...

# Task 4: Split data (80% train, 20% test)

# Task 5: Train a RandomForestClassifier and print the Accuracy Score.

print("--- Titanic Challenge Started ---")
# Start coding here...
