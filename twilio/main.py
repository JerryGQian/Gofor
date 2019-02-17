#!/usr/bin/env python
# import sqlite3
import json
import re
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# conn = sqlite3.connect('users.db')
# c = conn.cursor()

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    # number = request.values.get('from', None)
    # print(number)

    # t = (number,)
    # # c.execute('SELECT * FROM users WHERE num=?', t)
    # # print(c.fetchone())
    
    # """Respond to incoming messages with a friendly SMS."""
    # # Start our response
    # resp = MessagingResponse()

    # # Add a message
    # # resp.message("Hello! Meet the Gofor Analytics chat bot! Gofor is a service that uses the power of machine learning to predict future stock prices. Give me the name of a company to find their prospective stock prices.""")
    # resp.message(number)

    with open('hardcoded.json') as f:
        stocks = json.load(f)

    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    normalized = body.encode("ascii").lower()
    info = stocks.get(normalized)
    if "hey" in normalized or "hi" in normalized or "hello" in normalized:
        resp.message("Hello, I am Gofor! Tell me a company's stock symbol and I can predict their prices using machine learning.")
    elif info is not None:
        string = body.encode("ascii").upper() + "\n"
        string += "Date: " + info["date"] + "\n"
        string += "Low: " + str(round(info["low"], 2)) + "\n"
        string += "High: " + str(round(info["high"], 2)) + "\n"
        string += "Close: " + str(round(info["close"], 2))
        resp.message(string)
    else:
        resp.message("Please enter a valid stock symbol.")
        
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
