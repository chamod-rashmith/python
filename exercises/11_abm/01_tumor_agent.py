"""
Exercise: Agent-Based Tumor Growth (Grid Modeling)
Goal: Simulate a 2D tumor growing in a dish (Petri dish).
"""
import numpy as np
import matplotlib.pyplot as plt

# Rules:
# 1. Cells divide into empty neighbors with probability P_div.
# 2. Cells die spontaneously with probability P_death.
# 3. Cells move randomly (Diffusion) with probability P_move.

# Task 1: Setup 50x50 Grid.
N = 50
grid = np.zeros((N, N))

# Task 2: Seed 1 cell in the center.

# Task 3: Run the simulation loop for 500 steps.
# Update the grid based on rules.

# Task 4: Visualize the final tumor shape.
# Is it circular? Does it have a rough edge?

print("--- Agent-Based Tumor Challenge ---")
# Start coding here...
