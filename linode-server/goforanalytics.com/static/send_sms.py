from auth_token import account_sid, auth_token
from flask import Flask, request, redirect
from twilio.rest import Client

app = Flask(__name__)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    number = request.form['phonenumber']
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=number, 
        from_="+12402195388",
        body="Hello! Meet the Gofor Analytics chat bot! Gofor is a service that uses the power of machine learning to predict future stock prices. Give me the name of a company to find their prospective stock prices.")
    return ""
