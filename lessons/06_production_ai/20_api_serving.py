"""
Lesson 20: Serving AI via API (FastAPI)
Concept: Turning your trained model into a web service.
Why? AI models are useless if they stay on your computer. You need to serve them to users!
"""
from fastapi import FastAPI
import uvicorn
import numpy as np

# 1. Initialize our "API"
app = FastAPI(title="My First AI Service")

# 2. Simulate a trained model (in real life, you'd load a .pth or .pkl file)
def dummy_predict(hours_studied):
    # Predicts score: intercept + coefficient * hours
    return 10 + 5.5 * hours_studied

@app.get("/")
def home():
    return {"message": "Welcome to the AI Prediction API!"}

@app.get("/predict")
def predict(hours: float):
    # This is an API endpoint that users can call
    prediction = dummy_predict(hours)
    return {
        "hours_studied": hours,
        "predicted_score": round(prediction, 2)
    }

print("--- AI PRODUCTION LESSON ---")
print("FastAPI is the standard for high-performance Python APIs.")
print("To run this API yourself: uv run uvicorn lessons.06_production_ai.20_api_serving:app --reload")
print("\nTask: Imagine a world where your model predicts stock prices or identifies disease—this is how you'd serve it!")

if __name__ == "__main__":
    # In a real scenario, you'd run this from terminal
    print("Run `uvicorn lessons.06_production_ai.20_api_serving:app` to start the server.")
