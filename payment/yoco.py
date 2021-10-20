import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

Secret_Key = os.environ['yoco_SECRET_KEY']

def yocoPayment(token,amount):

    response = requests.post(
    'https://online.yoco.com/v1/charges/',
    headers={
        'X-Auth-Secret-Key': Secret_Key,
        },
    json={
        'token': token,
        'amountInCents': amount,
        'currency': 'ZAR',
        },
    )

    # response.status_code will contain the HTTP status code
    # response.json() will contain the response body
    return response.json