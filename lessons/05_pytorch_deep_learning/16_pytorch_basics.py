"""
Lesson 16: PyTorch Fundamentals
Concepts: Tensors, Gradient calculation (Autograd), and simple linear model.
Why? PyTorch is the primary tool used by AI researchers at Meta, Google, and OpenAI.
"""
import torch
import numpy as np

# 1. Tensors: The building block of Deep Learning
# Think of them as NumPy arrays, but they can run on GPUs and track gradients!
x = torch.tensor([[1, 2], [3, 4.]], requires_grad=True)
print(f"Tensor x:\n{x}")

# 2. Autograd: Magic of Backpropagation
y = x + 2
z = y * y * 3
out = z.mean()

print(f"\nForward pass result: {out}")

# Calculate gradients (Backprop)
out.backward()

# d(out)/dx
print(f"Gradients on x:\n{x.grad}")

# 3. Converting from NumPy
np_array = np.array([1, 2, 3])
torch_tensor = torch.from_numpy(np_array)
print(f"\nConverted from NumPy: {torch_tensor}")

# 4. A Simple Neural Network Layer
import torch.nn as nn

linear_layer = nn.Linear(in_features=5, out_features=2)
input_data = torch.randn(1, 5) # Random input
output = linear_layer(input_data)

print(f"\nLinear Layer Output: {output}")
print(f"Weights Shape: {linear_layer.weight.shape}")

print("\n--- Why PyTorch? ---")
print("1. Dynamic computation graphs: Change the model on the fly.")
print("2. GPU Acceleration: Move data to 'cuda' with .to('cuda').")
print("3. Industry Standard: Used for almost all modern LLMs.")
