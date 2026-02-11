"""
Lesson 3: Mathematical Oncology - Tumor Growth Models
Goal: Simulate the classic 'Gompertzian Growth' and basic Chemotherapy.
Why? Tumors don't grow forever; they slow down as they vascularize (or fail to).
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define Model: dN/dt = rN ln(K/N) - c(t)N
# N: Number of cells, r: Growth rate, K: Carrying capacity
# c(t): Chemotherapy drug effect (killing rate)
def chemotherapy(t):
    """Simple pulsed chemotherapy: Drug valid during certain intervals."""
    # Drug administered every 10 days for 2 days
    if (t % 10) < 2:
        return 0.8  # Strong killing effect
    return 0.0

def tumor_growth(t, N, r, K):
    drug = chemotherapy(t)
    # Protection against log(0) or negative populations
    if N <= 0: return 0
    dNdt = r * N * np.log(K / N) - drug * N
    return dNdt

# 1. Parameter Set
r = 0.5   # Intrinsic growth rate
K = 1e9   # Max tumor size (number of cells ~1cm^3)
t_span = (0, 60) # 2 months
N0 = [1e4] # Small initial tumor

# 2. Simulation
solution = solve_ivp(tumor_growth, t_span, N0, args=(r, K), dense_output=True, max_step=0.1)

# 3. Visualization
t = np.linspace(0, 60, 1000)
N = solution.sol(t)[0]

plt.figure(figsize=(10, 6))
plt.semilogy(t, N, label="Tumor Size (log scale)", color='red') # Log scale is standard in biology
plt.title("Tumor Response to Pulsed Chemotherapy")
plt.xlabel("Days")
plt.ylabel("Cell Count (N)")
plt.axhline(K, color='gray', linestyle='--', label="Carrying Capacity")

# Highlight drug administration periods
drug_schedule = [chemotherapy(ti) > 0 for ti in t]
plt.fill_between(t, 1, K, where=drug_schedule, color='cyan', alpha=0.2, label='Chemo Active')

plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()

print("\n--- Math Oncology Concept ---")
print("Notice the 'sawtooth' pattern? The tumor regrows between doses.")
print("The goal of Mathematical Oncology is to find the optimal dosing schedule (T) to eradicate N -> 0.")
