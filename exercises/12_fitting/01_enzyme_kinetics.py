"""
Exercise: Enzyme Kinetics Fitting (Michaelis-Menten)
Goal: Fit d/dt[P] = Vmax * [S] / (Km + [S]) to experimental data.
"""
import numpy as np
from scipy.optimize import least_squares
import matplotlib.pyplot as plt

# The Data: Reaction Velocity (V) vs Substrate Concentration [S]
S = np.array([0.1, 0.5, 1.0, 2.0, 5.0, 10.0])
V_obs = np.array([0.05, 0.18, 0.25, 0.35, 0.45, 0.48])

# Model: V = Vmax * S / (Km + S)

# Task 1: Define 'michaelis_menten(s, vmax, km)' function.

# Task 2: Define Residual function (Obs - Pred).

# Task 3: Use 'scipy.optimize.least_squares' to find Vmax and Km.

# Task 4: Plot the theoretical curve against the data points.
# This confirms if your enzyme follows standard kinetics.

print("--- Enzyme Kinetics Fitting Challenge ---")
# Start coding here...
