from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def detect_emotion(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.4:
        return "happy"
    elif polarity < -0.4:
        return "sad"
    elif any(word in text.lower() for word in [
        "frustrated", "annoyed", "stuck", "difficult",
        "problem", "error", "can't", "cannot"
    ]):
        return "frustrated"
    else:
        return "neutral"

def get_response(emotion):
    responses = {
        "happy": "That's wonderful! I'm glad things are going well for you.",
        "sad": "I'm sorry you're feeling that way. I'm here to listen.",
        "frustrated": "That sounds frustrating. Let's work through it together.",
        "neutral": "I understand. Tell me a little more."
    }

    return responses.get(emotion, responses["neutral"])

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "")

    emotion = detect_emotion(user_message)

    bot_response = get_response(emotion)

    return jsonify({
        "user_message": user_message,
        "detected_emotion": emotion,
        "bot_response": bot_response
    })
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
