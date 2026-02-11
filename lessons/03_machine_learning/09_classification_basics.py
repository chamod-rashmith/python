"""
Lesson 9: Classification (Iris Dataset)
Predicting the species of a flower based on its measurements.
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Load built-in dataset
iris = load_iris()
X = iris.data
y = iris.target
print(f"Features: {iris.feature_names}")
print(f"Target Species: {iris.target_names}")

# 2. Split data into Training and Testing sets
# We train on 80% and test on 20% to see if the model actually learned!
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Initialize Classifier
clf = KNeighborsClassifier(n_neighbors=3)

# 4. Train
clf.fit(X_train, y_train)

# 5. Predict on the test set
y_pred = clf.predict(X_test)

# 6. Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Prediction Example
new_flower = [[5.1, 3.5, 1.4, 0.2]] # Measurements
prediction = clf.predict(new_flower)
print(f"Prediction for new flower: {iris.target_names[prediction][0]}")
