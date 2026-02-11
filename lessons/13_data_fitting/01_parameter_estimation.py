"""
Lesson 1: Parameter Estimation (Fitting ODEs to Data)
Goal: Use `scipy.optimize.minimize` to find parameters (e.g. tumor growth rate) from patient data.
Why? In research, you almost NEVER know 'r' or 'K'. You must infer them from noisy experiments.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# 1. Generate Synthetic Patient Data (Ground Truth: k=0.5)
# Model: Exponential Growth (Simple Oncology)
# dN/dt = k * N
true_k = 0.5
initial_N = 10.0
time_points = np.array([0, 2, 4, 6, 8, 10])
noise = np.random.normal(0, 5.0, len(time_points)) # Adds realism
observed_N = initial_N * np.exp(true_k * time_points) + noise

# 2. Define Model Function (Must take 't' and 'params')
def model_prediction(t, k, N0):
    return N0 * np.exp(k * t)

# 3. Define Objective Function (Loss = Sum of Squared Errors)
def objective(params):
    k_guess, N0_guess = params
    # Predict with current guess
    predicted_N = model_prediction(time_points, k_guess, N0_guess)
    # Calculate Error
    sse = np.sum((predicted_N - observed_N)**2)
    return sse

# 4. Optimization Loop (Fitting)
initial_guess = [0.1, 5.0] # Poor guess
result = minimize(objective, initial_guess, method='Nelder-Mead')

estimated_k, estimated_N0 = result.x
print(f"True k: {true_k}, Estimated k: {estimated_k:.4f}")
print(f"True N0: {initial_N}, Estimated N0: {estimated_N0:.4f}")

# 5. Visualization
t_smooth = np.linspace(0, 10, 100)
fit_curve = model_prediction(t_smooth, estimated_k, estimated_N0)

plt.figure(figsize=(8, 5))
plt.scatter(time_points, observed_N, label='Noisy Patient Data', color='red')
plt.plot(t_smooth, fit_curve, label=f'Model Fit (k={estimated_k:.2f})', color='blue')
plt.title("Parameter Estimation (Inverse Problem)")
plt.xlabel("Time (Days)")
plt.ylabel("Tumor Size")
plt.legend()
plt.show()

print("\n--- Math Bio Research Skill ---")
print("This is called 'Inverse Modeling'. It's how we validate models against real-world biology.")
