from flask import Flask, render_template, request, jsonify
import pickle
import re
import nltk

from nltk.corpus import stopwords

nltk.download('stopwords')

app = Flask(__name__)

# Load model
model = pickle.load(open('models/model.pkl', 'rb'))

vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))

# Preprocessing
stop_words = set(stopwords.words('english'))

def preprocess(text):

    text = text.lower()

    text = re.sub(r'<.*?>', '', text)

    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()

    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# Home route
@app.route('/')

def home():

    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])

def predict():

    data = request.get_json()

    review = data['review']

    cleaned_review = preprocess(review)

    vector_input = vectorizer.transform([cleaned_review])

    prediction = model.predict(vector_input)[0]

    if prediction == 1:

        result = "😊 Positive Sentiment"

    else:

        result = "😔 Negative Sentiment"

    return jsonify({
        'sentiment': result
    })

if __name__ == '__main__':

    app.run(debug=True)