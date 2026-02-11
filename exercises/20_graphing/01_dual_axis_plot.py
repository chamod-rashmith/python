"""
Exercise: Publication Quality Plotting (Recreating Nature/Science Figures)
Goal: Use subplots, twin axes, and formatting.
"""
import matplotlib.pyplot as plt
import numpy as np

# Data (Climate Change Simulation - Synthetic)
years = np.arange(1950, 2050)
co2 = 300 + 0.1*(years-1950) + 0.02*(years-1950)**2 + np.random.normal(0, 5, 100)
temp = 14 + 0.01*(years-1950) + 0.0005*(years-1950)**2 + np.random.normal(0, 0.1, 100)

# Task 1: Create a Figure with 2 Y-Axes (CO2 on left, Temp on right)
# Use 'ax1.twinx()'

# Task 2: Plot CO2 as a Bar Chart (alpha=0.3, blue) on left axis.

# Task 3: Plot Temperature as a Line (red, thick) on right axis.

# Task 4: Add Error Bands (Temperature +/- 0.2 deg C) using 'fill_between'.
# ax2.fill_between(years, temp-0.2, temp+0.2, color='red', alpha=0.1)

# Task 5: Add Legends, Correct Labels (ppm vs °C), and Title.
# Make it look like a NYTimes graph!

print("--- Plotting Challenge (Dual Axis) ---")
# Start coding here...
