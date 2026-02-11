"""
Lesson 3: Introduction to 3D Plotting (Matplotlib mplot3d)
Goal: Visualize Fitness Landscapes and Spatial Biology.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 1. Generate Surface Data (Fitness Landscape)
# Z = Fitness, X, Y = Chemical Concentration
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y) # Create a grid for 3D

# Fitness Function: Multi-peaked landscape
# High fitness at (0,0), valleys around it
Z = np.sin(np.sqrt(X**2 + Y**2)) * np.cos(Y)

# 2. Setup Figure (3D Projection)
fig = plt.figure(figsize=(12, 6))

# Subplot 1: 3D Surface
ax1 = fig.add_subplot(121, projection='3d')
# plot_surface is standard for landscapes
# cmaps: viridis, plasma, magma, cividis (perceptually uniform)
surf = ax1.plot_surface(X, Y, Z, cmap='viridis', 
                        linewidth=0, antialiased=True)
ax1.set_title("Fitness Landscape (Surface)")
ax1.set_xlabel("Drug A Concentration")
ax1.set_ylabel("Drug B Concentration")
ax1.set_zlabel("Growth Rate (Fitness)")

# Add a color bar
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=5)

# Subplot 2: 3D Wireframe (Often clearer for shape)
ax2 = fig.add_subplot(122, projection='3d')
wire = ax2.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color='gray')
ax2.set_title("Grid Structure (Wireframe)")
ax2.view_init(elev=60, azim=30) # Change camera angle

plt.tight_layout()
plt.show()

print("\n--- Plotting Lesson ---")
print("1. Use `plot_surface` for continuous data (Landscapes).")
print("2. Use `plot_wireframe` or `contour` to see structure clearly.")
print("3. `rstride/cstride` controls grid density (Don't set too low or it turns black!).")
