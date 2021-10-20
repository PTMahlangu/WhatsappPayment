import os
import aiml
from dotenv import load_dotenv
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from payment.yoco import yocoPayment


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('yoco.html')


@app.route('/pay', methods=['POST'])
def reply():

    token = request.get_json()["token"]
    amount = request.get_json()["amount"]

    return yocoPayment(token,amount)



