import requests
from requests.structures import CaseInsensitiveDict
import json

url = "https://sandbox.test-simplexcc.com/wallet/merchant/v2/quote"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "apikey eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJ0bmVyIjoid2FsbGV4IiwiaXAiOlsiICAiXSwic2FuZGJveCI6dHJ1ZX0.Q8c3tymYLt-iy0ZzPQPLleFJIawFZZyYjfoDTq-d5Rs"
headers["Content-Type"] = "application/json"

data = """
{
    "end_user_id": "d7a13b22-a86c-41e3-9a21-115c4cc9b1af",
    "digital_currency": "BTC",
    "fiat_currency": "USD",
    "requested_currency": "USD",
    "requested_amount": 950,
    "wallet_id": "wallex",
    "payment_methods" : ["credit_card"]
}
"""

def dollartobitrun():
   resp = requests.post(url, headers=headers, data=data)
   print(resp.status_code)
   # for the whole output:
   read = resp.json()
   print(json.dumps(read, indent=4, sort_keys=True))
