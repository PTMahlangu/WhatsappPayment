import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Anonymous test key. Replace with your key.
SECRET_KEY = os.environ['yoco_SECRET_KEY']

def yocoPayment(token):
    response = requests.post(
    'https://online.yoco.com/v1/charges/',
    headers={
        'X-Auth-Secret-Key': SECRET_KEY,
    },
    json={
        'token': token,
        'amountInCents': 2799,
        'currency': 'ZAR',
    },
    )
    print(response.json())
    return response.json()
    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     return "Error initialize. Please try again."



