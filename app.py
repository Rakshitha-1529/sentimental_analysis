from flask import Flask, render_template, request, jsonify
import pickle
import re
import os
import nltk

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


# Create Flask application
app = Flask(__name__)


# ---------------------------------------------------
# Load Model and Vectorizer
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "models", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)

with open(vectorizer_path, "rb") as file:
    vectorizer = pickle.load(file)


# ---------------------------------------------------
# Load Stop Words
# ---------------------------------------------------

try:
    # Try to use NLTK stopwords
    stop_words = set(stopwords.words("english"))

except LookupError:
    # If NLTK stopwords are not available,
    # use sklearn's built-in English stopwords.
    stop_words = set(ENGLISH_STOP_WORDS)


# ---------------------------------------------------
# Text Preprocessing
# ---------------------------------------------------

def preprocess(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Keep only alphabets
    text = re.sub(r"[^a-zA-Z]", " ", text)

    # Split into words
    words = text.split()

    # Remove stopwords
    words = [
        word for word in words
        if word not in stop_words
    ]

    # Join words back into a sentence
    return " ".join(words)


# ---------------------------------------------------
# Home Route
# ---------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------------------------------
# Prediction Route
# ---------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        if not data or "review" not in data:
            return jsonify({
                "error": "Please provide a review."
            }), 400

        review = data["review"]

        # Preprocess review
        cleaned_review = preprocess(review)

        # Convert text into vector
        vector_input = vectorizer.transform([cleaned_review])

        # Predict sentiment
        prediction = model.predict(vector_input)[0]

        if prediction == 1:
            result = "😊 Positive Sentiment"
        else:
            result = "😔 Negative Sentiment"

        return jsonify({
            "sentiment": result
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ---------------------------------------------------
# Run Application
# ---------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
