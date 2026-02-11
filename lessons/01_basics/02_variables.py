"""
Lesson 2: Variables and Data Types
Concepts: int, float, str, bool, and type conversion.
"""

# Integers and Floats
age = 25
height = 5.9
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {height} (Type: {type(height)})")

# Strings
greeting = "Hello Python!"
print(f"Greeting: {greeting} (Type: {type(greeting)})")

# Boolean
is_learning = True
print(f"Is Learning: {is_learning} (Type: {type(is_learning)})")

# Type Conversion (Casting)
string_num = "100"
converted_num = int(string_num)
print(f"Converted '{string_num}' to {converted_num} (Type: {type(converted_num)})")

# Multiple Assignments
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

print("\nTask: Predict what happens if you try to convert 'abc' to an int.")
