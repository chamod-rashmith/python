"""
Exercise: Stochastic Viral Spread (Infection Noise)
Goal: Compare a deterministic SIR model vs a Stochastic SIR (Gillespie).
"""
import numpy as np
import matplotlib.pyplot as plt

# SIR Model (Stochastic Events):
# 1. Infection: S + I -> 2I (Rate: beta * S * I / N)
# 2. Recovery: I -> R (Rate: gamma * I)

# Task 1: Initialize Parameters
# N = 100
# I0 = 1
# beta = 1.0
# gamma = 0.2

# Task 2: Implement Gillespie Algorithm for SIR.
# Events: Infection, Recovery.
# Propensities: a1 (Infection), a2 (Recovery).

# Task 3: Run the simulation 10 times and plot all trajectories on one graph.
# Show how "randomness" can lead to disease extinction early on!

print("--- Stochastic SIR Challenge Started ---")
# Start coding here...
