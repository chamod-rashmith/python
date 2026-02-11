"""
Lesson 6: Visualizing Flow (Vector Fields & Streamplots)
Goal: Plotting Phase Portraits for Dynamical Systems (Predator-Prey).
Why? This is the STANDARD way to visualize stability in Math Bio.
"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Define the Grid (The "State Space")
# X = Prey, Y = Predator
x = np.linspace(0, 5, 20)
y = np.linspace(0, 5, 20)
X, Y = np.meshgrid(x, y)

# 2. Define the System (Lotka-Volterra)
# dX/dt = alpha*X - beta*X*Y
# dY/dt = delta*X*Y - gamma*Y
alpha, beta, delta, gamma = 1.0, 0.5, 0.5, 2.0

U = alpha*X - beta*X*Y  # X-component of velocity vector
V = delta*X*Y - gamma*Y # Y-component of velocity vector

# Normalize arrows so they don't look huge
speed = np.sqrt(U**2 + V**2)
U_norm = U / speed
V_norm = V / speed

# 3. Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# A. Quiver Plot (Arrows)
# Shows magnitude and direction at specific points
Q = ax1.quiver(X, Y, U_norm, V_norm, speed, cmap='autumn', pivot='mid')
ax1.set_title("Quiver Plot (Vector Field)")
ax1.set_xlabel("Prey Population")
ax1.set_ylabel("Predator Population")
fig.colorbar(Q, ax=ax1, label='Speed of Change')

# B. Streamplot (Fluid Flow Lines)
# Shows trajectories (Orbits). Much cleaner for complex systems.
st = ax2.streamplot(x, y, U, V, density=1.5, color=speed, cmap='winter', linewidth=1.5)
ax2.set_title("Streamplot (Trajectories)")
ax2.set_xlabel("Prey Population")
ax2.set_ylabel("Predator Population")
fig.colorbar(st.lines, ax=ax2, label='Speed')

# Add Nullclines (Where dX/dt = 0 or dY/dt = 0)
# dX/dt = 0 => X=0 or Y=alpha/beta = 2
ax2.axhline(alpha/beta, color='k', linestyle='--', alpha=0.5, label='X-Nullcline')
# dY/dt = 0 => Y=0 or X=gamma/delta = 4
ax2.axvline(gamma/delta, color='k', linestyle=':', alpha=0.5, label='Y-Nullcline')
ax2.legend()

plt.tight_layout()
plt.show()

print("\n--- Math Bio Visualization ---")
print("1. Quiver plots show instantaneous direction (Velocity).")
print("2. Streamplots show the path a system would take over time.")
print("3. Nullclines help identify 'Fixed Points' (Equilibria).")
