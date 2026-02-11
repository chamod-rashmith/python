"""
Exercise: Drug Diffusion in 2D Tissue
Goal: Simulate Chemotherapy spreading from a blood vessel.
"""
import numpy as np
import matplotlib.pyplot as plt

# 2D Diffusion Equation:
# dC/dt = D * (d^2C/dx^2 + d^2C/dy^2) - K * C

# Task 1: Setup a 50x50 Grid (Tissue)
N = 50

# Task 2: Initial Condition
C = np.zeros((N, N))
# Set Blood Vessel (Source) at center: C[25, 25] = 100.0 (Concentration)
# Or maybe a line of vessels: C[:, 25] = 100.0

# Task 3: Simulation Loop (Finite Difference)
# Laplacian in 2D: (Left + Right + Up + Down - 4*Center) / dx^2

# Task 4: Visualize Result (Using plt.imshow)
# Show how far the drug penetrates into the tissue.

# Bonus: Add "Tumor Cells" that die if C > threshold.

print("--- 2D Spatial Diffusion Challenge ---")
# Start coding here...
