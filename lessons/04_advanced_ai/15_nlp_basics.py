"""
Lesson 15: NLP (Natural Language Processing) Basics
Concepts: Toykenization, Stopwords, and Vectorization (TF-IDF).
Why? To process text for sentiment analysis, spam detection, or LLMs.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Simple Text Data
texts = [
    "I love this course, it is amazing!",
    "Python is the best programming language.",
    "I hate being stuck in traffic.",
    "This movie was terrible and boring.",
    "ML is fascinating and fun.",
    "The weather is bad today."
]
labels = [1, 1, 0, 0, 1, 0] # 1: Positive, 0: Negative

# 2. Text Vectorization (Converting words to math)
# TF-IDF stands for Term Frequency-Inverse Document Frequency
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

print("Vocabulary size:", len(vectorizer.get_feature_names_out()))
print("Example vector for first sentence:\n", X[0].toarray())

# 3. Simple Model (Naive Bayes - Great for text)
clf = MultinomialNB()
clf.fit(X, labels)

# 4. Predict Sentiment
new_text = ["This lesson is very helpful and great."]
new_X = vectorizer.transform(new_text)
prediction = clf.predict(new_X)

sentiment = "Positive" if prediction[0] == 1 else "Negative"
print(f"\nText: {new_text[0]}")
print(f"Predicted Sentiment: {sentiment}")

print("\n--- NLP Connection ---")
print("This is the 'Old School' way. Modern AI uses 'Embeddings' and 'Transformers' (like GPT).")
