"""
Exercise: Leaky Integrate-and-Fire (LIF) Neuron
Goal: Simulate the simplest spiking neuron model.
"""
import numpy as np
import matplotlib.pyplot as plt

# LIF Model Logic:
# dV/dt = -(V - V_rest) / tau + R * I_ext
# If V >= V_threshold, then:
#    Reset V -> V_reset
#    Record a spike time

# Task 1: Define Parameters
# tau = 10 ms (Time constant)
# R = 1.0 (Resistance)
# V_rest = -70 mV
# V_reset = -70 mV
# V_thresh = -55 mV
# I_ext = 20.0 (Input current)

# Task 2: Simulation Loop (Euler Method)
# dt = 0.1 ms, Time = 100 ms

# Task 3: Store Voltage history and Spike Times.

# Task 4: Plot Voltage vs Time. Draw dashed line for Threshold.

# Bonus: Create a 'Refractory Period' (Neuron can't fire for 2ms after spike).

print("--- LIF Neuron Challenge ---")
# Start coding here...
