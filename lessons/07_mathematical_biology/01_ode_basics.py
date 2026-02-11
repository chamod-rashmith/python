"""
Lesson 1: Solving ODEs - The Foundation of Math Bio
Goal: Learn scipy.integrate.solve_ivp. 
Example: The classic Logistic Growth Model (Population Biology).
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the differential equation: dN/dt = rN(1 - N/K)
def logistic_growth(t, N, r, K):
    """
    Args:
    t: time vector (required by solve_ivp)
    N: Population Size (state variable)
    r: Growth Rate
    K: Carrying Capacity
    """
    dNdt = r * N * (1 - N / K)
    return dNdt

# 1. Provide Parameters
r = 0.5  # Growth rate per day
K = 100  # Carrying capacity (max population)
t_span = (0, 50)  # Time from day 0 to 50
N0 = [10]  # Initial population (list because state vector)

# 2. Solve the Initial Value Problem (IVP)
solution = solve_ivp(logistic_growth, t_span, N0, args=(r, K), dense_output=True)

# 3. Access Results
t = np.linspace(0, 50, 100) # Generating 100 points for smooth plot
N = solution.sol(t)[0] # Interpolate solution at these points

# 4. Visualize
plt.figure(figsize=(10, 6))
plt.plot(t, N, label="Logistic Growth (Numeric)", color='blue', linewidth=2)
plt.axhline(K, color='red', linestyle='--', label="Carrying Capacity (K)")
plt.title("Population Growth: Logistic Model")
plt.xlabel("Time (Days)")
plt.ylabel("Population (N)")
plt.legend()
plt.grid(True)
plt.show()

print("\n--- Math Bio Concept ---")
print("This model is fundamental in oncology too: Tumors initially grow exponentially but slow down as they run out of nutrients (Carrying Capacity).")
