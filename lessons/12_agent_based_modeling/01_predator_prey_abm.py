"""
Lesson 1: Agent-Based Modeling (ABM)
Goal: Simulate an Ecosystem or Tumor (Cells moving on a grid).
Why? ODEs assume "Perfect Mixing" (all cells touch all nutrients). That's fake.
ABMs model individual Agents (Cells, Animals) moving and interacting.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Grid Parameters
GRID_SIZE = 50
steps = 200

# 2. Agent Types
# 0: Empty
# 1: Prey (Green) - Moves randomly, reproduces
# 2: Predator (Red) - Moves towards Prey, eats, dies if hungry

grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Seed Initial Population (Random)
grid[np.random.rand(GRID_SIZE, GRID_SIZE) < 0.2] = 1 # 20% Prey
grid[np.random.rand(GRID_SIZE, GRID_SIZE) < 0.05] = 2 # 5% Predator

# Helper: Get Neighbors
def get_neighbors(x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0: continue
            nx, ny = (x + dx) % GRID_SIZE, (y + dy) % GRID_SIZE # Periodic Boundary (Torus)
            neighbors.append((nx, ny))
    return neighbors

# 3. Simulation Loop
print("Running ABM Simulation... (This is slow in pure Python!)")
history = []

for s in range(steps):
    new_grid = grid.copy()
    
    # Iterate over all cells (Random order to avoid bias)
    agents = []
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x, y] > 0:
                agents.append((x, y))
    
    np.random.shuffle(agents)
    
    for x, y in agents:
        agent_type = grid[x, y]
        neighbors = get_neighbors(x, y)
        empty_spots = [n for n in neighbors if grid[n] == 0]
        prey_spots = [n for n in neighbors if grid[n] == 1]
        
        if agent_type == 1: # Prey
            # Check if eaten? (handled by predator logic)
            # Try to move or reproduce
            if empty_spots:
                target = empty_spots[np.random.choice(len(empty_spots))]
                if np.random.rand() < 0.1: # Reproduction
                    new_grid[target] = 1
                elif np.random.rand() < 0.5: # Move
                    new_grid[target] = 1
                    new_grid[x, y] = 0
                    
        elif agent_type == 2: # Predator
            if prey_spots:
                # Eat!
                target = prey_spots[np.random.choice(len(prey_spots))]
                new_grid[target] = 2 # Move into prey spot
                new_grid[x, y] = 0  
                # Reproduce if fed?
                if np.random.rand() < 0.5:
                    new_grid[x, y] = 2 # Leave child behind
            else:
                # Move Randomly & Starve
                if empty_spots:
                    target = empty_spots[np.random.choice(len(empty_spots))]
                    new_grid[target] = 2
                    new_grid[x, y] = 0
                
                # Starvation Check
                if np.random.rand() < 0.1:
                    new_grid[x, y] = 0 # Die
                    
            
    grid = new_grid
    if s % 2 == 0: history.append(grid.copy())

# 4. Visualization (Snapshot)
plt.figure(figsize=(6, 6))
plt.imshow(grid, cmap='nipy_spectral', interpolation='nearest') # Quick colormap check
plt.title(f"Agent-Based Model (Step {steps})")
plt.axis('off')
plt.show()

print("\n--- Math Bio Insight ---")
print("ABMs capture 'Emergent Behavior' (e.g., flocking birds, tumor heterogeneity).")
print("These are computationally heavy compared to ODEs.")
