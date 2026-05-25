const reviewInput = document.getElementById("review");
const resultOutput = document.getElementById("result");
const predictBtn = document.getElementById("predictBtn");
const sentimentMeter = document.getElementById("sentimentMeter");
const meterLabel = document.getElementById("meterLabel");

async function predictSentiment() {
    const review = reviewInput.value.trim();

    if (!review) {
        showResult('Please enter a review to analyze.', 'negative');
        updateMeter('none');
        return;
    }

    toggleLoading(true);

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ review })
        });

        if (!response.ok) {
            throw new Error('Unable to analyze sentiment.');
        }

        const data = await response.json();
        const sentiment = data.sentiment || 'Unable to determine sentiment.';
        const type = sentiment.includes('Positive') ? 'positive' : 'negative';

        showResult(sentiment, type);
        updateMeter(type);
    } catch (error) {
        showResult('Something went wrong. Try again.', 'negative');
        updateMeter('negative');
        console.error(error);
    } finally {
        toggleLoading(false);
    }
}

function showResult(message, sentimentType) {
    resultOutput.textContent = message;
    resultOutput.classList.remove('positive', 'negative', 'animate-positive', 'animate-negative');

    if (sentimentType) {
        resultOutput.classList.add(sentimentType);
        resultOutput.classList.add(sentimentType === 'positive' ? 'animate-positive' : 'animate-negative');
        setTimeout(() => {
            resultOutput.classList.remove('animate-positive', 'animate-negative');
        }, 900);
    }
}

function updateMeter(sentimentType) {
    sentimentMeter.style.width = sentimentType === 'positive' ? '100%' : sentimentType === 'negative' ? '100%' : '0%';
    sentimentMeter.style.background = sentimentType === 'positive' ? 'linear-gradient(135deg, #00d084, #47c9ff)' : sentimentType === 'negative' ? 'linear-gradient(135deg, #ff6a7a, #ff9d9d)' : 'transparent';
    meterLabel.textContent = sentimentType === 'positive' ? 'Positive mood detected' : sentimentType === 'negative' ? 'Negative mood detected' : 'Awaiting input';
}

function toggleLoading(isLoading) {
    if (isLoading) {
        predictBtn.textContent = 'Analyzing...';
        predictBtn.disabled = true;
    } else {
        predictBtn.textContent = 'Predict Sentiment';
        predictBtn.disabled = false;
    }
}

function clearReview() {
    reviewInput.value = '';
    showResult('Enter a review and click predict to see the sentiment.', '');
    updateMeter('none');
}
