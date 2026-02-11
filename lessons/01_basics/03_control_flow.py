"""
Lesson 3: Control Flow
Concepts: if statements, for loops, and while loops.
"""

# If Statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# For Loop (Range)
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# For Loop (List)
fruits = ["apple", "banana", "cherry"]
print("\nIterating through a list:")
for fruit in fruits:
    print(f"I like {fruit}s")

# While Loop
print("\nWhile loop counting down:")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

print("\nTask: Write a loop that prints only even numbers from 2 to 10.")
