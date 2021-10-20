
from flask import Flask, request
from controller import *

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Whatsapp payment integration"


@app.route('/message', methods=['POST'])
def reply():
    message = request.form.get('Body').lower()
    phone_no = request.form.get('From')

    WhatsappRespond(message,phone_no)



