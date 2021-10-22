import requests
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

    if response.status_code == 201:
        return response.content
    else:
        return {"msg":"error"}