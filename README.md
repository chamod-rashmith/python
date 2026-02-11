# 🧬 Python for Computational Biology & Mathematical Oncology

Welcome to the **Research Scientist Track**. This comprehensive curriculum is designed to take you from Python basics to simulating complex biological systems (Tumors, Neural Networks, Epidemics) and solving them with Modern AI.

---

## 📚 Complete Syllabus

### 🟢 Phase 1: Foundations of Scientific Computing
* **01_Basics**: Syntax, Variables, Control Flow.
* **02_Data_Science**: Mastering `pandas` and `numpy` for biological data.
* **03_Machine_Learning**: Scikit-Learn (Regression, Classification, Clustering).
* **04_Deep_Learning**: Neural Networks & PyTorch (The engine of AI).

### 🟡 Phase 2: Mathematical Modeling (The Core)
* **07_Mathematical_Biology**:
  * **01_ODE_Basics**: Simulating Population Growth (Logistic Model).
  * **02_Coupled_ODEs**: Predator-Prey Dynamics (Immune System vs Tumor).
  * **03_Tumor_Models**: Chemotherapy and Gompertzian Growth.
  * **04_Scientific_ML**: Solving ODEs with Neural Networks (PINNs).

### 🧠 Phase 3: Computational Neuroscience
* **08_Computational_Neuroscience**:
  * **01_FitzHugh_Nagumo**: Simulating Action Potentials (Spiking Neurons).
  * **02_Synaptic_Coupling**: Synchronization and Network Dynamics.

### 🌊 Phase 4: Spatial Biology (PDEs)
* **09_Spatial_Biology**:
  * **01_Tumor_Invasion**: Reaction-Diffusion models for cancer spread in tissue.
  * **02_Turing_Patterns**: How chemical reactions create biological structures (Spots/Stripes).

### 🎯 Phase 5: Advanced Optimization & Control
* **10_Advanced_Oncology**:
  * **01_Optimal_Control**: Designing the perfect Chemotherapy Schedule using `scipy.optimize`.

### 🎲 Phase 6: Stochastic & Agent-Based Modeling
* **11_Stochastic_Biology**:
  * **01_Gillespie_Algorithm**: Exact simulation of gene expression noise.
* **12_Agent_Based_Modeling**:
  * **01_Predator_Prey_ABM**: Simulating individual agents moving on a grid (Tumor Heterogeneity).

### 📈 Phase 7: Data Fitting (Inverse Problems)
* **13_Data_Fitting**:
  * **01_Parameter_Estimation**: Fitting ODE models to noisy patient data using optimization.

### 📊 Phase 8: Graphing Mastery (Visualization)
* **20_Graphing_Mastery**:
  * **20_Professional_2D**: Publication-quality plots (Matplotlib).
  * **21_Scientific_Plots**: Violin plots, Heatmaps, Dual-Axes.
  * **22_3D_Plots**: Surfaces and Wireframes (`mplot3d`).
  * **23_Interactive**: Rotatable 3D molecules (`plotly`).
  * **24_Vector_Fields**: Phase Portraits and Streamplots (Dynamical Systems).
  * **25_Animation**: Creating Movies of your simulations.
  * **26_Network_Graphs**: Visualizing Brain Connectomes & Gene Networks.

---

## �️ Tech Stack & Dependencies
* **Core**: `python`, `numpy`, `pandas`
* **Simulation**: `scipy` (Integrate, Optimize)
* **AI/ML**: `pytorch`, `scikit-learn`
* **Visualization**: `matplotlib`, `seaborn`, `plotly`, `networkx`

## 🚀 How to Run
Use the custom course launcher to navigate lessons and exercises:
```bash
uv run python main.py
```
