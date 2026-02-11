"""
Lesson 5: Interactive Biological Physics (Plotly)
Goal: Visualize Molecular Structures/Vector Fields in 3D.
Why Plotly? Matplotlib is static. Plotly lets you rotate, zoom, and explore (Crucial for Proteins).
"""
import plotly.graph_objects as go
import numpy as np

# 1. Generate 3D Trajectory (Random Walk in 3D / Polymer Folding)
np.random.seed(42)
steps = 500
x = np.cumsum(np.random.randn(steps))
y = np.cumsum(np.random.randn(steps))
z = np.cumsum(np.random.randn(steps))

# Add "Residue" colors along the path
colors = np.linspace(0, 1, steps)

# 2. Molecule (Line3D)
trace_backbone = go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines',
    line=dict(
        color=colors, # Color gradient (N-terminus to C-terminus)
        colorscale='Viridis',
        width=4
    ),
    name='Backbone'
)

# Add Atoms (Markers)
trace_atoms = go.Scatter3d(
    x=x[::10], y=y[::10], z=z[::10], # Only show every 10th atom
    mode='markers',
    marker=dict(
        size=8,
        color=colors[::10],
        colorscale='Plasma',
        opacity=0.8
    ),
    name='Alpha Carbons'
)

# 3. Layout (Look like PyMOL)
layout = go.Layout(
    title='Interactive Protein Folding Simulation',
    scene=dict(
        xaxis=dict(title='X (Å)'),
        yaxis=dict(title='Y (Å)'),
        zaxis=dict(title='Z (Å)'),
        aspectmode='data'
    ),
    width=900,
    height=700,
    margin=dict(l=0, r=0, b=0, t=40)
)

fig = go.Figure(data=[trace_backbone, trace_atoms], layout=layout)

# Show! (Opens in Browser)
fig.show()

print("--- Plotly Interaction ---")
print("1. Click & Drag to Rotate.")
print("2. Scroll to Zoom.")
print("3. Double-Click to Reset.")
print("Use Plotly for creating interactive HTML reports for collaborators.")
