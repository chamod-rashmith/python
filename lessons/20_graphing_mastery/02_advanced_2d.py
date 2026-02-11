"""
Lesson 2: Advanced 2D (Subplots, Error Bars, Annotations)
Goal: Creating complex multi-panel figures for Biology.
"""
import matplotlib.pyplot as plt
import numpy as np

# Data: Drug effectiveness experimental results
# Group A (Control), Group B (Treatment)
x_vals = np.array([1, 2, 3, 4, 5])
y_A = np.array([10, 15, 20, 25, 30])
y_B = np.array([10, 20, 35, 45, 60])
errors = np.array([1, 1.5, 2, 2.5, 3]) # Standard Deviation

# 1. Figure Setup (2x1 Layout: Top/Bottom)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10), sharex=True)

# 2. Plot 1: Error Bars
# Crucial for Biology: Always show variation!
ax1.errorbar(x_vals, y_A, yerr=errors, fmt='o-', 
             color='gray', ecolor='black', capsize=4, label='Control')
ax1.errorbar(x_vals, y_B, yerr=errors*2, fmt='s--', 
             color='red', ecolor='darkred', capsize=4, label='Drug Treatment')

ax1.set_title("Experimental Results: Drug X vs Control")
ax1.set_ylabel("Tumor Volume (mm³)")
ax1.legend()
ax1.grid(True, alpha=0.3)

# 3. Plot 2: Log Scale & Annotations
# Often biological growth is exponential, so Log(Y) makes it linear.
ax2.plot(x_vals, y_B, 'rs--', label='Drug Response')
ax2.set_yscale('log') # Logarithmic Y-axis
ax2.set_ylabel("Tumor Volume (Log Scale)")
ax2.set_xlabel("Weeks Post-Treatment")

# Add significant marker (p-value, asterisk)
ax2.annotate('Breakout Phase (*)', 
             xy=(4, 45), xytext=(2.5, 50),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='blue')

# Custom Tick Labels
plt.xticks(x_vals, ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"])

plt.tight_layout() # Fix overlap issues
plt.show()

print("\n--- Plotting Lesson ---")
print("1. Error Bars are non-negotiable in Bio experimental data.")
print("2. Log Scales reveal exponential growth patterns clearly.")
print("3. Subplots allow you to tell a multi-part story.")
