"""
Lesson 3.5: Object-Oriented Programming (OOP)
Why? In ML libraries like Scikit-Learn, models are objects.
You 'instantiate' a model, 'fit' it, and 'predict'.
"""

class SimpleModel:
    def __init__(self, name):
        self.name = name
        self.is_trained = False
        print(f"Model '{self.name}' initialized.")

    def train(self, data):
        print(f"Training '{self.name}' on data: {data}...")
        self.is_trained = True
        print("Training complete.")

    def predict(self, input_val):
        if not self.is_trained:
            return "Error: Train the model first!"
        return f"Prediction for {input_val}: [SUCCESS]"

# Usage
my_model = SimpleModel("LinearRegressionStub")
print(my_model.predict(10))

my_model.train([1, 2, 3, 4, 5])
print(my_model.predict(10))

print("\n--- ML Connection ---")
print("Every Scikit-Learn model (like RandomForestClassifier) follows this pattern!")
