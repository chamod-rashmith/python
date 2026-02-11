"""
Lesson 2: Neural Network Synchronization (Coupled Neurons)
Goal: Simulate two FitzHugh-Nagumo neurons connected by a Synapse.
Why? The brain is a network, not a single neuron. Synchronization = Consciousness/Seizures/Thinking.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Model: Two Coupled Neurons
# dV1/dt = V1 - V1^3/3 - W1 + I1 + Coupling * (V2 - V1)
# dW1/dt = phi * (V1 + a - bW1)
# dV2/dt = V2 - V2^3/3 - W2 + I2 + Coupling * (V1 - V2)
# dW2/dt = phi * (V2 + a - bW2)

def coupled_network(t, state, I1, I2, coupling_strength, phi, a, b):
    V1, W1, V2, W2 = state
    
    # Neuron 1 Dynamics
    dV1 = V1 - (V1**3)/3 - W1 + I1 + coupling_strength * (V2 - V1)
    dW1 = phi * (V1 + a - b*W1)
    
    # Neuron 2 Dynamics
    dV2 = V2 - (V2**3)/3 - W2 + I2 + coupling_strength * (V1 - V2)
    dW2 = phi * (V2 + a - b*W2)
    
    return [dV1, dW1, dV2, dW2]

# 1. Setup - Neuron 2 is slightly faster/driven harder (I2 > I1)
I1 = 0.5
I2 = 0.51 # Slightly different frequencies
coupling = 0.1 # Weak coupling. Try changing to 0.0 or 0.5!

phi = 0.08
a = 0.7
b = 0.8

state0 = [-1, 1, -1, 1] # Start synchronized
t_span = (0, 200)

solution = solve_ivp(coupled_network, t_span, state0, 
                     args=(I1, I2, coupling, phi, a, b), dense_output=True, max_step=0.1)

# 2. Visualization
t = np.linspace(0, 200, 2000)
sol = solution.sol(t)
V1, W1, V2, W2 = sol

plt.figure(figsize=(12, 6))

# Plot both neuron voltages
plt.subplot(2, 1, 1)
plt.plot(t, V1, 'b-', label='Neuron 1', alpha=0.7)
plt.plot(t, V2, 'r--', label='Neuron 2', alpha=0.7)
plt.title(f"Coupled Neural Network (Coupling Strength = {coupling})")
plt.xlabel("Time")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid(True)

# Phase Difference Plot (Synchronization)
plt.subplot(2, 1, 2)
plt.plot(t, V1-V2, 'k-')
plt.title("Synchronization Error (V1 - V2)")
plt.xlabel("Time")
plt.ylabel("Difference")
plt.grid(True)

plt.tight_layout()
plt.show()

print("\n--- Computational Neuroscience Insight ---")
print("1. With Coupling=0.0, they will strict drift out of phase.")
print("2. With Coupling=0.1, they might 'Lock' phases (Synchronization) despite different I inputs.")
print("This is exactly how your heart cells beat in unison!")
