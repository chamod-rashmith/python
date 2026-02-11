"""
Lesson 14: Introduction to Deep Learning
Concepts: Multi-Layer Perceptrons (Neural Networks).
Why? Neural Networks can learn complex patterns that simple math cannot.
"""
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load hand-written digits data (MNIST style)
digits = load_digits()
X, y = digits.data, digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Build a Neural Network (Multi-Layer Perceptron)
# hidden_layer_sizes=(64, 32) means 2 layers with 64 and 32 neurons.
mlp = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, alpha=1e-4,
                    solver='adam', verbose=False, random_state=1,
                    learning_rate_init=.01)

print("Training Neural Network... (this may take a moment)")
mlp.fit(X_train, y_train)

# 3. Predict & Show Results
print(f"Neural Network Accuracy: {mlp.score(X_test, y_test)*100:.2f}%")

# 4. Confusion Matrix (See where the model gets confused)
y_pred = mlp.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Neural Network: Handwritten Digit Confusion Matrix')
plt.show()

print("\n--- Deep Learning Intro ---")
print("An MLP is a 'shallow' deep learning model. For images, we use CNNs. For text, we use Transformers.")
