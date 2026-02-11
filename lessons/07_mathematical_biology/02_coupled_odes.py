"""
Lesson 2: Multidimensional ODEs (Compartment Models)
Goal: Lotka-Volterra Predator-Prey System.
This is the core of "Coupled Systems" in Ecology and Oncology (Tumor vs Immune System).
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the Equations:
# dP/dt = alpha*P - beta*P*K (Prey dynamics)
# dK/dt = delta*P*K - gamma*K (Predator dynamics)
def predator_prey(t, state, alpha, beta, delta, gamma):
    P, K = state  # P: Prey, K: Predator
    dPdt = alpha * P - beta * P * K
    dKdt = delta * P * K - gamma * K
    return [dPdt, dKdt]

# 1. Biological Parameters
alpha = 1.0  # Prey birth rate
beta = 0.1   # Predation rate (how fast predators eat P)
delta = 0.05 # Predator reproduction rate (from eating)
gamma = 0.5  # Predator death rate

# 2. Setup
state0 = [40, 9]  # Initial (Prey, Predator) population
t_span = (0, 200)

solution = solve_ivp(predator_prey, t_span, state0, args=(alpha, beta, delta, gamma), dense_output=True)

# 3. Time Series Plot
t = np.linspace(0, 200, 1000)
sol = solution.sol(t)
P, K = sol

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, P, label='Prey', color='green')
plt.plot(t, K, label='Predator', color='red')
plt.title("Predator-Prey Dynamics")
plt.xlabel("Time")
plt.legend()
plt.grid(True)

# 4. Phase Portrait (Crucial for Dynamical Systems!)
# This shows the "Orbit" or "Limit Cycle" of the system.
plt.subplot(1, 2, 2)
plt.plot(P, K, color='purple', lw=1.5)
plt.plot([state0[0]], [state0[1]], 'ro', label='Start') # Mark start point
plt.title("Phase Plane (Trajectory)")
plt.xlabel("Prey Population")
plt.ylabel("Predator Population")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("\n--- Math Bio Concept ---")
print("1. Phase Portraits help visualize if a system crashes (extinction) or oscillates forever.")
print("2. In Oncology: Prey = Tumor Cells, Predator = Immune/Chemo Agent.")
