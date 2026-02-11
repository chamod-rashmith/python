"""
Lesson 1: Optimal Control in Oncology (Chemotherapy Optimization)
Goal: Minimize Final Tumor Size (N) subject to Toxicity constraints.
We use `scipy.optimize.minimize` to find the best drug schedule.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# 1. Model Dynamics (Gompertz Growth with Drug Killing)
def tumor_dynamics(t, N, doses, dose_times, r, K, kill_strength):
    # Find active dose at time t
    # Assume dose lasts for 1 day
    current_drug = 0.0
    for i, dose_time in enumerate(dose_times):
        if dose_time <= t < dose_time + 1.0:
            current_drug = doses[i]
            break
            
    if N <= 1e-6: return 0 # Tumor eradicated
    
    # dN/dt = rN ln(K/N) - alpha * C(t) * N
    dNdt = r * N * np.log(K/N) - kill_strength * current_drug * N
    return dNdt

# 2. Objective Function (To Minimize)
# We want to minimize: Final Tumor Size + Penalty * Total Drug Usage
def objective(doses, *args):
    r, K, kill_strength, N0, t_span, dose_times, toxicity_limit = args
    
    # Constraint: Doses must be non-negative
    if np.any(doses < 0): return 1e9
    
    # Constraint: Total Drug < Limit
    total_drug = np.sum(doses)
    if total_drug > toxicity_limit: return 1e9
        
    # Solve ODE
    sol = solve_ivp(tumor_dynamics, t_span, [N0], 
                    args=(doses, dose_times, r, K, kill_strength),
                    method='RK45')
    
    final_tumor_size = sol.y[0][-1]
    
    return final_tumor_size

# 3. Optimization Setup
r = 0.5
K = 1e9
kill_strength = 1.2
N0 = 1e7
t_span = (0, 30) # 30 Days
toxicity_limit = 5.0 # Max total units of drug allowed

# Suppose we can give 5 doses at fixed times
dose_times = [0, 5, 10, 15, 20] 
initial_doses = np.ones(5) # Start with uniform dosing

# Run Optimization
print("Optimizing Chemotherapy Schedule... (This may take a moment)")
result = minimize(objective, initial_doses, 
                  args=(r, K, kill_strength, N0, t_span, dose_times, toxicity_limit),
                  bounds=[(0, 2) for _ in range(5)], # Max single dose = 2
                  method='SLSQP')

optimal_doses = result.x

print("\n--- Optimization Results ---")
print(f"Optimal Doses: {np.round(optimal_doses, 2)}")
print(f"Total Drug Used: {np.sum(optimal_doses):.2f} (Limit: {toxicity_limit})")

# 4. Simulate & Plot Result
sol = solve_ivp(tumor_dynamics, t_span, [N0], 
                args=(optimal_doses, dose_times, r, K, kill_strength), dense_output=True)
t = np.linspace(0, 30, 200)
N = sol.sol(t)[0]

plt.figure(figsize=(10, 5))
plt.semilogy(t, N, 'r-', linewidth=2, label='Tumor Size')
plt.ylabel("Tumor Cells (Log Scale)")
plt.xlabel("Days")
plt.title("Optimized Chemotherapy Schedule")

# Plot Doses
for i, time in enumerate(dose_times):
    plt.bar(time, optimal_doses[i], width=0.8, color='blue', alpha=0.3, label='Chemo Dose' if i==0 else "")

plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()

print("\n--- Mathematical Oncology Insight ---")
print("Notice how the optimizer might choose 'Metronomic Dosing' (constant low doses) vs 'Maximum Tolerated Dose' (spikes).")
