"""
Lesson 4: Scientific Plotting (Heatmaps, Categorical Plots, Seaborn)
Goal: Visualize complex biological data (Heatmaps for Genomes, Violins for Distributions).
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Load sample dataset (Gene Expression in different tissues)
# We can use built-in datasets or create synthetic.
# Let's use Seaborn "iris" to simulate gene expression.
try:
    df = sns.load_dataset('iris')
    df.columns = ["Gene A", "Gene B", "Gene C", "Gene D", "Tissue Type"] # Renamed for bio
except:
    # Synthetic data if no internet
    df = pd.DataFrame(np.random.normal(5, 2, (100, 4)), 
                      columns=["Gene A", "Gene B", "Gene C", "Gene D"])
    df["Tissue Type"] = np.random.choice(["Liver", "Kidney", "Brain"], 100)

# Setup plotting grid
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 1. Heatmap (Correlation Matrix)
# Which genes are co-expressed?
corr = df.iloc[:, :4].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax1)
ax1.set_title("Co-Expression Correlation Matrix")

# 2. Violin Plot (Distribution of Gene A across Tissues)
# Shows density + median (box plot)
sns.violinplot(x="Tissue Type", y="Gene A", data=df, inner='quartile', ax=ax2, palette='Pastel1')
sns.swarmplot(x="Tissue Type", y="Gene A", data=df, color='black', alpha=0.5, size=3, ax=ax2) # Individual points
ax2.set_title("Gene A Expression Distribution (Violin + Swarm)")
ax2.set_ylabel("Expression Level (Log2)")

plt.show()

print("\n--- Plotting Lesson ---")
print("1. Heatmaps are standard for Correlation/Distance (e.g., Clustering).")
print("2. Violin Plots are superior to Box Plots for showing distribution shape (e.g., 'bimodal').")
print("3. Swarm Plots show raw data points, which is honest reporting.")
