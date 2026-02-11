"""
Lesson 1: Professional 2D Plotting (Basic Matplotlib)
Goal: Creating Publication-Quality Plots for Reasearch.
"""
import matplotlib.pyplot as plt
import numpy as np

# Set the style to something professional
# Available styles: 'default', 'classic', 'ggplot', 'seaborn', 'fivethirtyeight', etc.
try:
    plt.style.use('seaborn-v0_8-paper')
except:
    plt.style.use('ggplot')

# 1. Generate Data (Example: Enzyme Activity over Time)
x = np.linspace(0, 10, 100)
y1 = np.sin(x) * np.exp(-0.1*x)  # Damped oscillation
y2 = np.cos(x) * np.exp(-0.1*x)

# 2. Basic Figure & Axes
# Use plt.subplots() (Most flexible way)
fig, ax = plt.subplots(figsize=(8, 6))

# 3. Plotting
# Line styles: '-', '--', '-.', ':'
# Markers: 'o', 's', '^', 'x', '*'
ax.plot(x, y1, 'b-', label='Activator (Enzyme A)', linewidth=2)
ax.plot(x, y2, 'r--', label='Inhibitor (Enzyme B)', linewidth=2)

# 4. Customization
ax.set_title("Enzyme Dynamics: Activation vs Inhibition", fontsize=14, fontweight='bold')
ax.set_xlabel("Time (minutes)", fontsize=12)
ax.set_ylabel("Activity Level", fontsize=12)
ax.axhline(0, color='gray', linestyle=':', linewidth=1) # Zero line

# Legend
ax.legend(loc='upper right', frameon=True, shadow=True)

# Grid
ax.grid(True, linestyle='--', alpha=0.6)

# Spines (top/right borders) removal for cleaner scientific look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 5. Saving (Crucial for Papers!)
# Support PDF (vector), PNG (raster), SVG (web)
plt.savefig("plot_example.png", dpi=300, bbox_inches='tight')

plt.show()

print("\n--- Plotting Lesson ---")
print("1. Always label your axes (Units!).")
print("2. Use distinct line styles for B&W printing.")
print("3. Export as PDF or 300dpi PNG for journals.")
