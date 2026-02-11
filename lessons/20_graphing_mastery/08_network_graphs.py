"""
Lesson 8: Network Graphs (Nodes & Edges) - NetworkX
Goal: Visualize Protein-Protein Interactions (PPI) or Brain Connectomes.
Why? Biology is a network (Signaling Pathways, Metabolic Webs).
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# 1. Create a Biological Network (Random Scale-Free Graph)
# Scale-Free: Most biological networks follow Power Law (Hub genes).
# The Barabási-Albert model generates scale-free graphs.
G = nx.barabasi_albert_graph(20, 2) # 20 Nodes, each new node connects to 2 existing

# Add Node Attributes (e.g., Gene Importance)
# Centrality: How "connected" is a node?
centrality = nx.degree_centrality(G)
# Color nodes by centrality
node_colors = [centrality[n] for n in G.nodes()]

# Add Edges Attributes (Interaction Strength)
edge_widths = [1 + np.random.rand() * 2 for _ in G.edges()]

# 2. Visualize with nx.draw
plt.figure(figsize=(10, 8))

# Layout Algorithm: Fruchterman-Reingold (Spring Layout)
# Simulates repulsive forces between nodes, attractive forces along edges.
pos = nx.spring_layout(G, k=0.15, iterations=20)

# Draw Nodes
nx.draw_networkx_nodes(G, pos, 
                       node_size=[v * 1000 for v in centrality.values()], # Size depends on connectivity
                       node_color=node_colors, 
                       cmap=plt.cm.coolwarm, 
                       alpha=0.9)

# Draw Edges
nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.5, edge_color='gray')

# Draw Labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

plt.title("Gene Interaction Network (Scale-Free)", fontsize=16)
plt.axis('off')
plt.show()

print("\n--- Network Visualization Lesson ---")
print("1. Scale-Free networks often have 'Hubs' (essential genes).")
print("2. Layout algorithms (Spring, Circular, Spectral) matter for readability.")
print("3. NetworkX integrates with Matplotlib easily.")
