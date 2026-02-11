"""
Lesson 2: Turing Patterns (Reaction-Diffusion)
Goal: Simulate how simple chemistry creates complex patterns (Stripes/Spots).
Why? This explains how animal coats (zebras, leopards) and even tumor angiogenesis form.
"""
import numpy as np
import matplotlib.pyplot as plt

# Gray-Scott Model (Simplified Turing System)
# Two Chemicals: U (Activator), V (Inhibitor)
# dU/dt = Du * Lap(U) - UV^2 + F(1-U)  (Feed Rate F)
# dV/dt = Dv * Lap(V) + UV^2 - (F+k)V  (Kill Rate k)

# 1. Grid Parameters
N = 100
dx = 1.0
Du = 0.16
Dv = 0.08
F = 0.035
k = 0.060
dt = 1.0
T = 2000

# 2. Initial Condition
U = np.ones((N, N))
V = np.zeros((N, N))

# Add a small square of V to start the reaction in the middle
mid = N//2
r = 10
# Perturbation
U[mid-r:mid+r, mid-r:mid+r] = 0.50
V[mid-r:mid+r, mid-r:mid+r] = 0.25

# Adding random noise to break symmetry
U += np.random.normal(0, 0.02, (N, N))
V += np.random.normal(0, 0.02, (N, N))

# 3. Laplacian Function (Using FFT or Conv2D is faster, but let's do simple Finite Difference)
def laplacian(Z):
    # This is a discrete 5-point stencil for the 2D Laplacian
    # Top + Bottom + Left + Right - 4*Center
    L = -4*Z
    L += np.roll(Z, (0, -1), (0, 1)) # Right neighbor
    L += np.roll(Z, (0, 1), (0, 1))  # Left neighbor
    L += np.roll(Z, (-1, 0), (0, 1)) # Top neighbor
    L += np.roll(Z, (1, 0), (0, 1))  # Bottom neighbor
    return L

print("Simulating Reaction-Diffusion... (This takes a few seconds)")

# 4. Main Loop
frames = []
for i in range(T):
    Lu = laplacian(U)
    Lv = laplacian(V)
    
    # Reaction Dynamics (Gray-Scott)
    uvv = U * V * V
    
    dU = (Du * Lu - uvv + F * (1 - U)) * dt
    dV = (Dv * Lv + uvv - (F + k) * V) * dt
    
    U += dU
    V += dV
    
    if i % 50 == 0:
        frames.append(V.copy())

# 5. Visualization
plt.figure(figsize=(6, 6))
plt.imshow(V, cmap='inferno', interpolation='bicubic')
plt.title(f"Turing Pattern (F={F}, k={k})")
plt.axis('off')
plt.show()

print("\n--- Developmental Biology Concept ---")
print("These 'Spots' emerge spontaneously from randomness due to Reaction-Diffusion instability.")
print("Alan Turing (yes, the Computer Science father) discovered this in 1952!")
