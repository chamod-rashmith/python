"""
Exercise: Hyperparameter Hunter
Goal: Use GridSearchCV to find the best parameters for a Support Vector Machine (SVM).
"""
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

# 1. Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Task 1: Initialize a Support Vector Classifier (SVC).

# Task 2: Create a param_grid with:
# 'C': [0.1, 1, 10]
# 'kernel': ['linear', 'rbf']

# Task 3: Use GridSearchCV with 3-fold cross-validation.

# Task 4: Print the best parameters and the best score.

print("--- Hyperparameter Hunter Challenge ---")
# Start coding here...
