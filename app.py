import os
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from payment.payment import initializePayment

load_dotenv()
app = Flask(__name__)

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
client = Client(account_sid, auth_token)

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route('/')
def home():
    return 'welcome to whatsappbot payment'

@app.route('/message', methods=['POST'])
def reply():
    message = request.form.get('Body').lower()

    phone_no = request.form.get('From')
    url = initializePayment()["data"]["authorization_url"]

    if message == "done":
        return respond(f'Danko! your payment was successfully.')

    if message:
        return respond(f'Please click the link to complete payment and reply *done*: '+ url)

