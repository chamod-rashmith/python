"""
Lesson 17: Convolutional Neural Networks (CNNs)
Concepts: Convolutions, Pooling, and Image Classification.
Why? CNNs are how AI 'sees' images. They are vastly more efficient than MLPs for vision.
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

# 1. Define the CNN Architecture
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Convolutional layers find patterns like edges and shapes
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10) # 10 classes (digits 0-9)

    def forward(self, x):
        # Apply Conv -> Pooling -> Activation
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        # Flatten for the fully connected layers
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

# 2. Setup the model
model = SimpleCNN()
print("Model Architecture:")
print(model)

# 3. Explain the mechanism
print("\n--- How a CNN Works ---")
print("1. Conv Layer: Slides a small filter over the image to detect features.")
print("2. Pooling: Reduces the image size, focusing on the strongest signals.")
print("3. Activation (ReLU): Decides if a neuron should 'fire'.")
print("4. Fully Connected (FC): Makes the final decision based on detected features.")

print("\nTask: In a real training loop, you would use torch.optim.SGD or Adam to update weights.")
print("This model has over 20,000 parameters learning to recognize digits!")
