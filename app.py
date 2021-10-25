import os
import aiml
import json
from dotenv import load_dotenv
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from payment.yoco import yocoPayment


load_dotenv()

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
client = Client(account_sid, auth_token)
kernel = aiml.Kernel()

for filename in os.listdir("brain"):
	if filename.endswith(".aiml"):
		kernel.learn("brain/" + filename)


app = Flask(__name__)


def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)


@app.route('/')
def home():
    user_amount = 6200
    return render_template('yoco.html',data=json.dumps(user_amount))


@app.route('/yoco', methods=['POST'])
def reply():

    inData = request.get_json()

    print(inData)
    return ""



