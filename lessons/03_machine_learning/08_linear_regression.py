"""
Lesson 8: Your First ML Model (Linear Regression)
We will predict House Prices based on Square Footage.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Prepare Data (House Size in SqFt, Price in $1000s)
# Note: Scikit-learn expects 2D array for X (features)
X = np.array([500, 700, 1000, 1200, 1500, 2000, 2500]).reshape(-1, 1)
y = np.array([150, 200, 250, 300, 380, 450, 600])

print("Features (X): \n", X)
print("Target (y): ", y)

# 2. Initialize the Model
model = LinearRegression()

# 3. Train the Model (Fit)
model.fit(X, y)

# 4. Predict
new_house = np.array([[1800]])
prediction = model.predict(new_house)
print(f"\nPredicted price for a 1800 sqft house: ${prediction[0]:.2f}k")

# 5. Visualize (Optional)
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title("House Price Prediction")
plt.xlabel("Square Footage")
plt.ylabel("Price ($1000s)")
plt.legend()
plt.show()

print("\n--- ML Vocabulary Learned ---")
print("1. Features (X): The data you use to predict.")
print("2. Target (y): The data you want to predict.")
print("3. Fit: The process of 'learning' from the data.")
print("4. Predict: Using the learned model on new data.")
