import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
Secret_Key = os.environ['paystack_Secret_Key']

def initializePayment():
    url = "https://api.paystack.co/transaction/initialize"

    payload = json.dumps({
    "email": "mahlangu@email.com",
    "amount": "30000",
    "currency": "ZAR",
    "metadata": {
        "custom_fields": [
        {
            "display_name": "Mobile Number",
            "variable_name": "mobile_number",
            "value": "+27727082628"
        }
        ]
    }
    })
    
    headers = {
    'Authorization': f'Bearer {Secret_Key}',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error initialize. Please try again."




# https://documenter.getpostman.com/view/2770716/paystack-api/7187aMn