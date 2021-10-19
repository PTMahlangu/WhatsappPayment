import os
import aiml
from dotenv import load_dotenv
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from payment.paystack import initializePayment
from payment.yoco import yocoPayment

load_dotenv()

# Create the kernel and learn AIML files
# kernel = aiml.Kernel()

# for filename in os.listdir("brain"):
# 	if filename.endswith(".aiml"):
# 		kernel.learn("brain/" + filename)


# while True:
#     msg =input("Enter inpuet :")
#     reply = kernel.respond(msg)
#     print(reply)

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
    return "welcome to whatsapp payment integration"

@app.route('/yoco')
def yoco_home():
    return render_template('home.html')

@app.route('/pay',methods=['POST'])
def yoco_pay():
    data = request.json
    print(data["token"])
    return yocoPayment(data["token"])

@app.route('/message', methods=['POST'])
def reply():
    message = request.form.get('Body').lower()

    phone_no = request.form.get('From')

    url = initializePayment(phone_no)["data"]["authorization_url"]

    if message == "done":
        return respond(f'Danko! your payment was successfully.')

    if "pay" in message:
        return respond(f'Please click the link to complete payment and reply *done*: '+ url)

