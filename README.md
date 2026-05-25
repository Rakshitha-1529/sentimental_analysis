# Movie Review Sentiment Analysis

A clean Flask web app that classifies movie review text as positive or negative sentiment.

## Overview
This project demonstrates a simple sentiment analysis pipeline with a modern user interface.
It uses a trained TF-IDF vectorizer and Linear SVM model to make predictions from user input.

## Features
- Browser-based sentiment prediction for movie reviews
- Lightweight Flask backend with a JSON prediction endpoint
- Polished and responsive frontend layout
- Animated feedback for positive and negative sentiment results

## Project structure
- `app.py` — Flask server and prediction endpoint
- `templates/index.html` — app frontend
- `static/style.css` — visual styling
- `static/script.js` — frontend interactivity and API calls
- `models/model.pkl` — trained sentiment model
- `models/vectorizer.pkl` — saved TF-IDF vectorizer
- `data/IMDB Dataset.csv` — original dataset used for training

## Requirements
Install dependencies in a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requriments.txt
```

## Run the app
Start the Flask server:

```powershell
python app.py
```

Open in the browser:

```text
http://127.0.0.1:5000
```

## Usage
- Enter a movie review in the text box
- Click **Predict Sentiment**
- View the sentiment result and animated feedback

## Notes for GitHub
- Keep `venv/` out of version control.
- The `.gitignore` file already excludes common environment, IDE, and model/data files.
- If you want, you can push the repository to GitHub with a simple `git init`, `git add .`, `git commit`, and `git push`.

## Optional improvements
- Add model retraining support inside the app
- Add more sentiment classes or confidence scores
- Deploy to a cloud host like Heroku, Render, or Railway
