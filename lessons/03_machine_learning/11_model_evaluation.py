"""
Lesson 11: Professional Model Evaluation
Concepts: Cross-Validation and GridSearchCV (Hyperparameter Tuning).
Why? To ensure your model isn't just 'memorizing' data (Overfitting).
"""
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits

# 1. Load data
digits = load_digits()
X, y = digits.data, digits.target

# 2. Cross-Validation: Testing the model on different 'folds' of data
# Instead of one test set, we test it 5 times on different parts.
model = RandomForestClassifier(n_estimators=50)
scores = cross_val_score(model, X, y, cv=5)
print(f"Cross-Validation Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")

# 3. Grid Search: Finding the BEST 'knobs' (hyperparameters) for your model
# Should we use 50 trees? 100? What max depth?
param_grid = {
    'n_estimators': [10, 50, 100],
    'max_depth': [None, 5, 10]
}

print("\nStarting Grid Search (this may take a few seconds)...")
grid_search = GridSearchCV(model, param_grid, cv=3)
grid_search.fit(X, y)

print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Score: {grid_search.best_score_:.4f}")

print("\n--- ML Tip ---")
print("Grid Search is the 'Gold Standard' for perfecting a model before deployment.")
