from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load the pre-trained model for emotion detection
emotion_model = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# Emoji mapping
EMOJI_MAP = {
    "joy": "😊",
    "sadness": "😢",
    "anger": "😡",
    "fear": "😨",
    "love": "❤️",
    "surprise": "😲",
    "disgust": "🤢",
    "neutral": "😐"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect-emotion', methods=['POST'])
def detect_emotion():
    # Get input text from the request
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Predict the emotion
    result = emotion_model(text)
    top_emotion = result[0]['label']
    emoji = EMOJI_MAP.get(top_emotion, "🤔")  # Default emoji

    # Return the result
    return jsonify({
        "text": text,
        "emotion": top_emotion,
        "emoji": emoji,
        "confidence": result[0]['score']
    })

if __name__ == '__main__':
    app.run(debug=True)
