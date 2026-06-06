# Empathetic AI Chatbot

A simple chatbot prototype that detects user emotions and responds empathetically.

## Features

- Emotion Detection
- Sentiment Analysis
- REST API
- Flask Backend

## Installation

```bash
git clone https://github.com/yourusername/empathetic-chatbot.git

cd empathetic-chatbot

pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Server starts at:

http://127.0.0.1:5000

## API Example

POST /chat

Request:

```json
{
  "message": "I am really happy today!"
}
```

Response:

```json
{
  "user_message": "I am really happy today!",
  "detected_emotion": "happy",
  "bot_response": "That's wonderful! I'm glad things are going well for you."
}
```
