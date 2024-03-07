# Import logging module
import logging
from flask import Flask, request
from chat import chat_with_gpt
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

app.config['SERVER_NAME'] = '0c3e-168-228-50-229.ngrok-free.app'

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Define a global variable to track whether the message has been sent
message_sent = False

@app.route("/webhook", methods=["POST"])
def webhook():
    global message_sent  # Use the global keyword to modify the global variable

    # Initialize a Twilio MessagingResponse
    twiml_response = MessagingResponse()

    # Check if the message has already been sent
    if not message_sent:
        # Set the flag to indicate that the message has been sent
        message_sent = True

        # Extract incoming message from request payload
        incoming_message = request.form.get("Body")
        
        # Log incoming message
        logging.debug("Incoming message: %s", incoming_message)
        
        # Process incoming message with ChatGPT
        response = chat_with_gpt(incoming_message)
        
        # Log response
        logging.debug("ChatGPT response: %s", response)

        twiml_response.message(str(response))
        
        # Return the TwiML response as a string
        return str(twiml_response)
    else:
        # If the message has already been sent, return a message indicating that
        return "The message has already been processed."

if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)
