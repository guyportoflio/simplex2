import json

import requests
from requests.structures import CaseInsensitiveDict

url = "https://sandbox.test-simplexcc.com/wallet/merchant/v2/payments/partner/data"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "apikey eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJ0bmVyIjoid2FsbGV4IiwiaXAiOlsiICAiXSwic2FuZGJveCI6dHJ1ZX0.Q8c3tymYLt-iy0ZzPQPLleFJIawFZZyYjfoDTq-d5Rs"
headers["Content-Type"] = "application/json"

data = """
{
        "account_details": {
            "app_provider_id": "wallex",
            "app_end_user_id": "48a09063-18a6-4d39-838f-6fd0c1c2a2f3",
            "app_version_id" : "1.3.1",
            "signup_login" : {
                "ip" : "212.179.111.110",
                "timestamp" : "2022-01-15T09:27:34.431Z"
            }
        },
        "transaction_details": {
            "payment_details": {
                "quote_id": "27cd308f-ea8d-4660-86f2-b1a2065c9c96",
                "payment_id": "56024b8e-8f9e-432c-a83b-6b40a9d8be92",
                "destination_wallet": {
                    "address" : "16HAsVHRcmGSxGHfFvq67zjQq8XjEQFvVr",
                    "currency" : "BTC"
                }
            }

        }

    }
"""

def paymentrequestrun():
  resp = requests.post(url, headers=headers, data=data)
  print("return code: " + str(resp.status_code))
  #for the whole output:
  read = resp.json()
  print(json.dumps(read, indent=4, sort_keys=True))