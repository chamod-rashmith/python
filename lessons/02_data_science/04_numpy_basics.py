"""
Lesson 4: NumPy Basics
NumPy (Numerical Python) is the foundational library for ML. 
It provides efficient multi-dimensional arrays.
"""
import numpy as np

# Creating arrays
arr = np.array([1, 2, 3, 4, 5])
print(f"Simple Array: {arr}")
print(f"Shape: {arr.shape}")

# 2D Arrays (Matrices) - Crucial for ML datasets
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nMatrix:\n{matrix}")
print(f"Matrix Shape: {matrix.shape}")

# Statistical operations
print(f"\nMean: {np.mean(arr)}")
print(f"Standard Deviation: {np.std(arr)}")
print(f"Max value: {np.max(arr)}")

# Math on arrays (Vectorization)
# In Python, you'd need a loop. In NumPy, it's instant!
arr_plus_10 = arr + 10
print(f"\nArray + 10: {arr_plus_10}")

# Useful for initialization
zeros = np.zeros((2, 3))
print(f"\nZeros (useful for weights initialization):\n{zeros}")

print("\n--- Why this matters for ML ---")
print("ML models treat data as matrices. NumPy makes matrix math incredibly fast.")
