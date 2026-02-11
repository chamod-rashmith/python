"""
Exercise: The Viral Outbreak Challenge (SIR Model)
Goal: Model an epidemic (Susceptible-Infected-Recovered).
This is the same math used for COVID-19 modeling.
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# The SIR Model Equations:
# dS/dt = -beta * S * I / N_total
# dI/dt = beta * S * I / N_total - gamma * I
# dR/dt = gamma * I

# Task 1: Define the 'sir_model' function.

# Task 2: Set parameters:
# N_total = 1000 (Total population)
# I0 = 1 (Initial infected case)
# R0 = 0 (Initial recovered)
# S0 = N_total - I0 - R0
# beta = 0.3 (Infection rate)
# gamma = 0.1 (Recovery rate ~ 10 days)

# Task 3: Solve the ODE for 160 days.

# Task 4: Plot S(t), I(t), and R(t).
# Identify the "Peak Infection" day.

# Bonus: Calculate the "Basic Reproduction Number" R0 = beta / gamma.
# If R0 > 1, the disease spreads.

print("--- Viral Outbreak Challenge (SIR Model) Started ---")
# Start coding here...
