"""
Exercise: Phase Portrait Challenge (The Saddle Node)
Goal: Plot Vector Field & Nullclines for a Bistable Switch.
"""
import numpy as np
import matplotlib.pyplot as plt

# A "Bistable Switch" (Gene Regulatory Network)
# dU/dt = U/(1+V^2) - U  (Feedback loop)
# dV/dt = V/(1+U^2) - V

# Task 1: Create a Grid (np.meshgrid) for U and V (0 to 3).

# Task 2: Calculate Vector Fields dU and dV.
# Normalize arrows for cleaner look.

# Task 3: Use 'ax.streamplot' to visualize the flow.
# Use coloring by speed.

# Task 4: Plot Nullclines (dU=0 => U = V/(1+V^2) or U=0)
# This requires solving implicitly or plotting implicitly.
# Hint: Just plot contour(U, V, dU, levels=[0])!
# And contour(U, V, dV, levels=[0]).

# Task 5: Identify STABLE and UNSTABLE fixed points.
# Mark them with circles (Empty for unstable, Filled for stable).

print("--- Phase Portrait Challenge ---")
# Start coding here...
