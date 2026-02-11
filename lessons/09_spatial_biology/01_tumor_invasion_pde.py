"""
Lesson 1: Reaction-Diffusion Systems (PDEs)
Goal: Simulate Spatial Tumor Invasion (Gompertz Growth + Diffusion).
Why? Tumors don't just grow in one spot—they invade surrounding tissue using enzymes.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Model: dU/dt = D * Laplacian(U) + Growth(U)
# U(x, t): Tumor density at position x and time t
# D: Diffusion coefficient (how fast cells move)
# Growth: Gompertzian rU * ln(K/U)

# 1. Spatial Grid Setup (1D Finite Difference)
L = 100         # Length of tissue (mm)
N = 100         # Number of spatial grid points
dx = L / (N - 1)  # Space step

T = 50          # Total time (days)
dt = 0.1        # Time step (must satisfy CFL condition for stability: D*dt/dx^2 < 0.5)
timesteps = int(T / dt)

# 2. Parameters
D = 1.0         # Diffusion rate
r = 0.5         # Growth rate
K = 100.0       # Carrying capacity

# 3. Initial Condition (Small tumor in the middle)
U = np.zeros(N)
U[45:55] = 10.0 # Seed 10 cells in the center 10 grid points

# History for animation
history = [U.copy()]

# 4. Main Simulation Loop (Finite Difference Method)
for step in range(timesteps):
    # Laplacian (Discrete 2nd Derivative): [1, -2, 1] kernel
    # U[i-1] - 2U[i] + U[i+1]
    # We use NumPy sliding window magic for speed (Vectorization!)
    laplacian = (np.roll(U, -1) - 2*U + np.roll(U, 1)) / (dx**2)
    
    # Boundary Conditions (No Flux / Neumann): Values at edges don't change by diffusion
    laplacian[0] = 0
    laplacian[-1] = 0
    
    # Reaction Term (Gompertz Growth)
    # Avoid log(0) issues
    growth = r * U * np.log(K / (U + 1e-9))
    
    # Update U:  New = Old + (Diffusion + Reaction) * dt
    change = (D * laplacian + growth) * dt
    U += change
    
    # Store every 10th frame for visualization
    if step % 10 == 0:
        history.append(U.copy())

# 5. Visualization (Space-Time Plot)
history = np.array(history)

plt.figure(figsize=(10, 6))
# Create a heatmap: Y-axis depends on Time, X-axis is Space
im = plt.imshow(history, aspect='auto', cmap='Reds', extent=[0, L, T, 0])
plt.colorbar(label='Tumor Density')
plt.title("Spatiotemporal Tumor Invasion (1D Reaction-Diffusion)")
plt.xlabel("Position (mm)")
plt.ylabel("Time (Days)")
plt.show()

print("\n--- Math Oncology Concept ---")
print("1. Notice how the tumor 'spreads' outward? That's Diffusion.")
print("2. Notice how the center gets darker (denser)? That's Growth.")
print("This is the foundation for modeling Glioblastoma (Brain Cancer) spread.")
