"""
Lesson 1: The FitzHugh-Nagumo Model (Neural Excitation)
Goal: Simulate an Action Potential (Spike) in a neuron.
Why? This is a simplified version of the Nobel Prize-winning Hodgkin-Huxley model.
It's a Dynamical System with 'Fast' and 'Slow' variables.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# System Equations:
# dV/dt = V - V^3/3 - W + I_ext (Membrane Potential)
# dW/dt = phi * (V + a - b*W)   (Recovery Variable)

def fitzhugh_nagumo(t, state, I_ext, phi, a, b):
    V, W = state
    dVdt = V - (V**3)/3 - W + I_ext
    dWdt = phi * (V + a - b * W)
    return [dVdt, dWdt]

# 1. Parameters
# These are standard dimensionless parameters
I_ext = 0.5  # External current (Stimulation)
phi = 0.08   # Controls the speed of the recovery (time scale separation)
a = 0.7
b = 0.8

# 2. Simulation (Two Scenarios: Resting vs Spiking)
t_span = (0, 100)
state0 = [-1.0, 1.0] # Initial state near rest

solution = solve_ivp(fitzhugh_nagumo, t_span, state0, args=(I_ext, phi, a, b), dense_output=True, max_step=0.1)

# 3. Visualization
t = np.linspace(0, 100, 1000)
sol = solution.sol(t)
V, W = sol

plt.figure(figsize=(12, 6))

# Time Series Plot (Voltage Trace)
plt.subplot(1, 2, 1)
plt.plot(t, V, label='Membrane Potential (V)', color='blue', lw=2)
plt.plot(t, W, label='Recovery Variable (W)', color='orange', linestyle='--')
plt.title(f"Neuron Action Potential (I_ext={I_ext})")
plt.xlabel("Time")
plt.ylabel("Voltage / Recovery")
plt.legend()
plt.grid(True)

# Phase Plane Analysis (Nullclines & Trajectory)
# Nullclines are where dV/dt = 0 or dW/dt = 0
v_null = np.linspace(-2.5, 2.5, 100)
w_null_V = v_null - (v_null**3)/3 + I_ext  # dV/dt = 0 -> W = V - V^3/3 + I
w_null_W = (v_null + a) / b             # dW/dt = 0 -> W = (V + a)/b

plt.subplot(1, 2, 2)
plt.plot(v_null, w_null_V, 'g--', label='V-Nullcline', alpha=0.6)
plt.plot(v_null, w_null_W, 'r--', label='W-Nullcline', alpha=0.6)
plt.plot(V, W, color='black', lw=2, label='Trajectory') # The Limit Cycle
plt.scatter([state0[0]], [state0[1]], color='red', zorder=5) # Start Point
plt.title("Phase Plane (Limit Cycle)")
plt.xlabel("V (Voltage)")
plt.ylabel("W (Recovery)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print("\n--- Computational Neuroscience Concept ---")
print("1. Notice the 'Limit Cycle' in the Phase Plane? That represents repetitive firing (Spiking).")
print("2. If I_ext is low, the system goes to a 'Fixed Point' (Resting State).")
print("   Try changing I_ext to 0.0 in the code and run again!")
