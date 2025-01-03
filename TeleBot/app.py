from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    # Get the message from the user
    incoming_msg = request.values.get('Body', '').strip().lower()

    # Create a Twilio MessagingResponse object
    resp = MessagingResponse()
    msg = resp.message()

    # Reply based on the message
    if incoming_msg == 'hi':
        msg.body("Hello! How can I assist you today?")
    else:
        msg.body("Sorry, I only respond to 'Hi' for now. Try saying 'Hi'!")

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
