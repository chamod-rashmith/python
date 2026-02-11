"""
Lesson 1: The Gillespie Algorithm (Stochastic Simulation)
Goal: Simulate random chemical reactions in a single cell.
Why? In Biology, gene expression is noisy! "Deterministic" ODEs fail when molecule counts are low.
"""
import numpy as np
import matplotlib.pyplot as plt

# Model: Simple Gene Expression
# DNA --> mRNA (Transcription check rate k1)
# mRNA --> Protein (Translation rate k2)
# mRNA --> degradation (rate d1)
# Protein --> degradation (rate d2) 

# 1. Provide Parameters
k1 = 2.0   # Transcription rate
k2 = 10.0  # Translation rate
d1 = 0.5   # mRNA decay
d2 = 0.2   # Protein decay

# 2. Initial State (Molecule Counts - Must be Integers!)
mRNA = 0
Protein = 0
time = 0.0
T_max = 50.0

# Store history
history_t = [0]
history_m = [0]
history_p = [0]

# 3. Gillespie Loop (Exact Stochastic Simulation)
print("Running Gillespie Simulation... (This may take a moment)")
while time < T_max:
    # A. Calculate Propensities (Reaction Rates * State)
    # Rate of DNA -> mRNA: k1 (Constant, DNA=1)
    # Rate of mRNA -> Protein: k2 * mRNA
    # Rate of mRNA -> Null: d1 * mRNA
    # Rate of Protein -> Null: d2 * Protein
    
    a1 = k1
    a2 = k2 * mRNA
    a3 = d1 * mRNA
    a4 = d2 * Protein
    
    a_total = a1 + a2 + a3 + a4
    
    if a_total == 0: break # No more reactions
    
    # B. Determine Time to Next Reaction (dt)
    # dt is exponentially distributed!
    r1 = np.random.random()
    dt = (1.0 / a_total) * np.log(1.0 / r1)
    
    time += dt
    
    # C. Determine WHICH reaction happens
    # We roll a weighted die
    r2 = np.random.random()
    threshold = r2 * a_total
    
    if threshold < a1:
        # Transcription
        mRNA += 1
    elif threshold < a1 + a2:
        # Translation
        Protein += 1
    elif threshold < a1 + a2 + a3:
        # mRNA Decay
        mRNA -= 1
    else:
        # Protein Decay
        Protein -= 1
        
    history_t.append(time)
    history_m.append(mRNA)
    history_p.append(Protein)

# 4. Visualization
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.step(history_t, history_m, where='post', color='blue', label='mRNA')
plt.title("Stochastic Gene Expression (Gillespie Algorithm)")
plt.ylabel("Molecule Count")
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 1, 2)
plt.step(history_t, history_p, where='post', color='green', label='Protein')
plt.xlabel("Time (min)")
plt.ylabel("Molecule Count")
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()

print("\n--- Math Bio Concept ---")
print("1. Notice the 'Burstiness' or noise? An ODE would just give a smooth average line.")
print("2. This noise is CRITICAL for cell decision making (e.g. Stem Cell differentiation).")
