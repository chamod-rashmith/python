"""
Lesson 7: Animation & Video Production (Matplotlib Animation)
Goal: Make movies of your models (Tumor Growth, Reaction-Diffusion).
Why? Biology is dynamic. A static plot misses the magic of time evolution.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Setup Simulation (1D Diffusion)
L = 100
N = 100
dx = L / (N - 1)
D = 1.0
dt = 0.05
timesteps = 200

x = np.linspace(0, L, N)
# Initial Condition: Sharp Square Wave ("Injected Concentration")
U = np.zeros(N)
U[40:60] = 1.0

# 2. Setup Plot
fig, ax = plt.subplots(figsize=(8, 5))
line, = ax.plot(x, U, 'r-', linewidth=2, label='Concentration U(x)')
ax.set_ylim(0, 1.2)
ax.set_title("Diffusion Process: t=0.00")
ax.set_ylabel("Concentration")
ax.set_xlabel("Position (x)")
ax.legend()
ax.grid(True)

# 3. Animation Function (Called every frame)
def update(frame):
    global U
    # Solve 1 step of PDE
    laplacian = (np.roll(U, -1) - 2*U + np.roll(U, 1)) / (dx**2)
    laplacian[0] = 0; laplacian[-1] = 0 # No Flux
    change = D * laplacian * dt
    U += change
    
    # Update Plot Data
    line.set_ydata(U)
    ax.set_title(f"Diffusion Process: t={frame*dt:.2f}")
    
    return line,

# 4. Create Animation
ani = animation.FuncAnimation(fig, update, frames=timesteps, interval=50, blit=True)

# 5. Saving (Requires ffmpeg for mp4, pillow for gif)
try:
    print("Saving Animation as GIF... (Wait)")
    ani.save("diffusion_movie.gif", writer='pillow', fps=30)
    print("Saved as 'diffusion_movie.gif'")
except:
    print("Could not save GIF (Pillow missing?) - Only showing plot.")

plt.show()

print("\n--- Animation Mastery ---")
print("1. FuncAnimation updates only the 'Line' object (Fast).")
print("2. You can save as MP4 (better quality) if you install FFmpeg: `sudo apt install ffmpeg`")
