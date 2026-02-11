"""
Final Exercise: The AI Architect Challenge
Goal: Build a full pipeline: Preprocess -> PCA -> Neural Network.
"""
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# 1. Load Real Dataset (Breast Cancer Diagnosis)
data = load_breast_cancer()
X, y = data.data, data.target

# --- YOUR TASKS ---

# Task 1: Scale the features using StandardScaler.
# (Neural Networks work MUCH better when data is between -1 and 1)

# Task 2: Reduce the 30 features to 5 using PCA.

# Task 3: Split the data into 80% Training and 20% Testing.

# Task 4: Train an MLPClassifier.

# Task 5: Print the final accuracy and the number of iterations it took to converge.

print("--- AI Architect Challenge Started ---")
# Start coding here...
