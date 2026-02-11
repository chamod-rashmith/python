"""
Lesson 10: Decision Trees & Random Forests
Concepts: Non-linear models and Ensembles.
Why? Random Forests are one of the most powerful 'out-of-the-box' ML models.
"""
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1. Generate Synthetic Data
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 2. Random Forest: An 'Ensemble' of many Decision Trees
# n_estimators is the number of trees.
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)

# 3. Train
print("Training Random Forest...")
rf.fit(X_train, y_train)

# 4. Feature Importance
# Which features actually mattered?
importances = rf.feature_importances_
print(f"\nTop Feature Importance: {importances[0]:.4f}")

# 5. Evaluate
y_pred = rf.predict(X_test)
print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred))

print("\n--- ML Tip ---")
print("Random Forests are 'robust'—they handle non-linear data and missing values better than simple regression!")
