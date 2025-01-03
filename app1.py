from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "7277992515:AAGNrtbNJLvhPCLlOhurHL1FTu3MSxfz0rs"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

@app.route('/telegram', methods=['POST'])
def telegram_webhook():
    data = request.json
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    
    
    if text.lower() == "hi":
        reply = "Hello! Here's a video you can watch:"
        send_message_with_button(chat_id, reply)  
    else:
        reply = "I'm a bot, and I didn't understand that. Try saying 'Hi'."
        send_message(chat_id, reply)
    
    return "OK"

def send_message(chat_id, text):
    payload = {"chat_id": chat_id, "text": text}
    requests.post(TELEGRAM_API_URL, json=payload)

def send_message_with_button(chat_id, text, button_text="Watch", button_url="https://youtu.be/a5378NPgb2Y?si=FDxl7Fr83kVQb6NB"):
    
    keyboard = {
        "inline_keyboard": [
            [   {
                    "text": button_text,
                    "url" : button_url
                }
            
            ],

            [
                {
                    "text": button_text,
                    "url": button_url
                }
            ]
        ]
    }

    # Send the message with the inline keyboard
    payload = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": keyboard
    }
    requests.post(TELEGRAM_API_URL, json=payload)

if __name__ == "__main__":
    app.run(port=5000)
