import os
import aiml
from dotenv import load_dotenv
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("yoco.html")


@app.route('/pay', methods=['POST'])
def reply():
    message = request.form.get('Body').lower()
    phone_no = request.form.get('From')

    token = request.form.get('token')

    print(token)
    return "Welcome to Whatsapp payment integration"



