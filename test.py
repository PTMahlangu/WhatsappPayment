import os
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


load_dotenv()


account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
client = Client(account_sid, auth_token)

message = client.messages.create(
         media_url=['https://sandstorm-mule-6634.twil.io/assets/image_from_ios.jpg'],
         from_='whatsapp:+14155238886',
         to='whatsapp:+27727082628'
     )

print(message.sid)