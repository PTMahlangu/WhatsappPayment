import os
import aiml
import json
from dotenv import load_dotenv
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from payment.paystack import initializePayment
from payment.yoco import yocoPayment

load_dotenv()

# Create the kernel and learn AIML files
kernel = aiml.Kernel()

for filename in os.listdir("brain"):
	if filename.endswith(".aiml"):
		kernel.learn("brain/" + filename)


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
    return "Welcome to Whatsapp payment integration " 


@app.route('/pay')
def yoco():
    # global user_amount
    # user_amount = 5200
    return render_template('yoco.html',data=json.dumps(user_amount))


@app.route('/yoco', methods=['POST'])
def yoco_pay():
    # global user_amount
    token = request.get_json()
    return yocoPayment(token,user_amount)


@app.route('/message', methods=['POST'])
def reply():
    global user_amount
    message = request.form.get('Body').lower()
    phone_no = request.form.get('From')

    if not message.isdigit():
        reply = kernel.respond(message)
    else:
        reply = kernel.respond("Pay "+message)

    if not reply:
        reply = "Oops! Something wrong. How much would you like to pay?"

    if kernel.getPredicate("amount"):
        user_amount = int(kernel.getPredicate("amount"))*100
        # url = initializePayment(phone_no,amount)["data"]["authorization_url"]
        url = str(request.url_roo) +"pay"
        kernel.setPredicate("url",url)

    return respond(reply)



