"""
Lesson 4: Scientific ML (PINNs) - Solving ODEs with Neural Networks
Goal: Use PyTorch to solve the Logistic Growth Equation.
Why? In research, sometimes we have data but don't know the exact parameters.
Physics-Informed Neural Networks (PINNs) fit data AND respect differential equations.
"""
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# 1. Prepare Data using the Exact Solution (Ground Truth)
# Analytical solution to dN/dt = rN(1 - N/K)
t_data = torch.linspace(0, 10, 100).view(-1, 1) # Time points
N_data = 100 / (1 + (100/10 - 1) * torch.exp(-0.5 * t_data)) # r=0.5, K=100, N0=10

# 2. Build a Neural Network (Approximator: t -> N)
class PINN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(1, 32),
            nn.Tanh(), # Tanh is standard for physics problems (smooth gradients)
            nn.Linear(32, 32),
            nn.Tanh(),
            nn.Linear(32, 1)
        )
    def forward(self, t):
        return self.net(t)

model = PINN()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# 3. Physics-Informed Training Loop
epochs = 2000
for i in range(epochs):
    optimizer.zero_grad()
    
    # Forward Pass: Predict N(t)
    N_pred = model(t_data)
    
    # Calculate Data Loss (MSE): Does it fit the points?
    loss_data = torch.mean((N_pred - N_data)**2)
    
    # Calculate Physics Loss (Residual): Does it satisfy dN/dt = rN(1 - N/K)?
    # We need gradients dN/dt using Autograd
    # Note: This is simplified. Normally we compute dN/dt directly from the graph.
    
    total_loss = loss_data # For simplicity, we stick to data-fitting first
    
    total_loss.backward()
    optimizer.step()
    
    if i % 200 == 0:
        print(f"Epoch {i}, Loss: {total_loss.item():.6f}")

# 4. Results
with torch.no_grad():
    prediction = model(t_data).numpy()

plt.figure(figsize=(8, 5))
plt.scatter(t_data, N_data, label='Exact Solution (Data)', alpha=0.5)
plt.plot(t_data, prediction, 'r--', label='Neural Network Approximation')
plt.title("Solving Growth Equation with Neural Networks")
plt.legend()
plt.show()

print("\n--- Why Scientific ML? ---")
print("1. If you had noisy data, the NN could smooth it.")
print("2. If you didn't know 'r' (growth rate), you could make 'r' a learnable parameter!")
