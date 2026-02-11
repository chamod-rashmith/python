"""
Lesson 12: Unsupervised Learning (Clustering & PCA)
Concepts: Finding patterns in data WITHOUT labels.
Why? Used for customer segmentation or simplifying huge datasets.
"""
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.datasets import load_wine

# 1. Load data (Wine dataset - 13 features)
data = load_wine()
X = data.data
y = data.target # We won't use 'y' for training (that's why it's unsupervised!)

# 2. PCA: Dimensionality Reduction
# We can't plot 13 dimensions. Let's squash them into 2!
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print(f"Original shape: {X.shape}")
print(f"Reduced shape (PCA): {X_reduced.shape}")

# 3. K-Means Clustering
# Let's tell the model to find 3 groups (clusters) in the wine data.
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
clusters = kmeans.predict(X)

# 4. Visualize the results
plt.figure(figsize=(10, 5))

# Plot PCA results colored by clusters
plt.subplot(1, 2, 1)
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=clusters, cmap='viridis')
plt.title("K-Means Clustering (after PCA)")
plt.xlabel("PC 1")
plt.ylabel("PC 2")

# Plot PCA results colored by original types (for comparison)
plt.subplot(1, 2, 2)
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='plasma')
plt.title("Original Labels (for comparison)")

plt.tight_layout()
plt.show()

print("\n--- ML Tip ---")
print("PCA is vital for 'Big Data' as it removes noise and speeds up training by reducing input size.")
