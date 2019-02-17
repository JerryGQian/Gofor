#!/usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Hello! Meet the Gofor Analytics chat bot! Gofor is a service that uses the power of machine learning to predict future stock prices. Give me the name of a company to find their prospective stock prices.""")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
