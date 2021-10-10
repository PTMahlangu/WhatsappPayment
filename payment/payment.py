import requests
import json

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
    'Authorization': 'Bearer sk_test_fd25ed2426ee5c9bca6b5c16dc74af2d1a46a807',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error initialize. Please try again."


# print(initializePayment()["data"]["authorization_url"])