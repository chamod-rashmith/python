"""
Lesson 5: Advanced Python Concepts
Concepts: List Comprehensions, Lambda Functions, and Decorators.
Why? You'll see these in clean ML code and data preprocessing pipelines.
"""
from colorama import Fore, Style

# 1. List Comprehensions (Faster and cleaner than for-loops)
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(f"Squares: {squares}")

# 2. Lambda Functions (Anonymous functions often used in Pandas)
# Example: Adding a simple calculation to a dataframe
multiply = lambda x, y: x * y
print(f"3 * 4 = {multiply(3, 4)}")

# 3. Decorators (Modify function behavior without changing code)
# Common use: Timing how long a model takes to train.
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{Fore.YELLOW}[Timer] {func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def heavy_computation():
    print("Simulating training a model...")
    time.sleep(1)
    return "Model Done"

heavy_computation()

print("\n--- ML Tip ---")
print("Lambda functions are huge in Pandas .apply() operations!")
