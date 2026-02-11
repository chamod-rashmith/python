"""
Exercise: 3D Heatmap & Contour (Energy Landscape)
Goal: Visualize potential energy surfaces (Chemistry/Biology)
"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Surface Data (Peaks and Valleys)
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2)) + 0.5 * np.exp(-((X-1)**2 + (Y-1)**2))

# Task 1: Create a figure with 2 subplots (1 wide, 2 tall)
# Top: 3D Surface (plot_surface)
# Bottom: 2D Contour (contourf)

# Task 2: Use Colormap 'plasma' or 'inferno'.

# Task 3: Add contours on the Bottom plot with 'levels=20'.
# Add labels (clabel) to the contours if possible.

# Task 4: Add a Colorbar that applies to both plots? Or just one?

# Important: Set 'aspect ratio' to equal for the contour plot.
# ax2.set_aspect('equal')

print("--- 3D Surface & Contour Challenge ---")
# Start coding here...
