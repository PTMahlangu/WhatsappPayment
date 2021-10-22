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


@app.route('/yoco')
def home():
    user_amount = 6200
    print('url:' +str(request.url_root)+"yoco")
    return render_template('yoco.html',data=json.dumps(user_amount))


@app.route('/pay', methods=['POST'])
def reply():

    token = request.get_json()["token"]
    amount = request.get_json()["amount"]

    return yocoPayment(token,amount)



