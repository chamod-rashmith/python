"""
Exercise: Customer Segmentation (Clustering)
Goal: Group 'Customers' based on their spending and income.
"""
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# 1. Sample Data (Annual Income vs Spending Score)
data = {
    'Income': [15, 16, 17, 18, 19, 20, 70, 71, 72, 80, 81, 82],
    'Spending': [39, 81, 6, 77, 40, 76, 50, 55, 60, 10, 12, 15]
}
df = pd.DataFrame(data)

# Task 1: Initialize KMeans with n_clusters=3.

# Task 2: Fit the model to the dataframe.

# Task 3: Add a 'Cluster' column to the dataframe with the predicted labels.

# Task 4: Visualize the results with a scatter plot (Income vs Spending), 
# colored by the Cluster.

print("--- Customer Segmentation Challenge ---")
# Start coding here...
