import requests
from requests.structures import CaseInsensitiveDict

url = "https://sandbox.test-simplexcc.com/payments/new"

headers = CaseInsensitiveDict()
headers["Authorization"] = "apikey eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJ0bmVyIjoid2FsbGV4IiwiaXAiOlsiICAiXSwic2FuZGJveCI6dHJ1ZX0.Q8c3tymYLt-iy0ZzPQPLleFJIawFZZyYjfoDTq-d5Rs"
headers["Content-Type"] = "text/html"

data = "version=1&partner=wallex&payment_flow_type=wallet&return_url_success=https%3A%2F%2Fwww.wallex.com&return_url_fail=https%3A%2F%2Fwww.wallex.com%2Fsupport&payment_id=67aa53c7-88ce-469b-9687-a681285727ef&="

session = requests.Session()

def paymentformrun():
  resp = session.post(url, headers=headers, data=data)
  print("return code: " + str(resp.status_code))
  r = requests.post(url, cookies={'uaid': 'Y%2BGzg%2BWBQ8xpOClOcdRElvAtRaq8biLJ3fgGEElsdE%2BAId6GX%2BNTbmmuMr6m5gMrz61JvAg8zvoo3tpvtkAvEDbh0R2t52YCZj%2F02RogB1znmcl%2FemkHKcYAHvej7jd%2Bq7hZ6nJZiz6MMLLJjaI5ooNJghj0KoIeu%2FiQdaf7YfM%3D'})
  print(r.cookies)
  #for the whole output:
  #read = resp.json()
  #print(json.dumps(read, indent=4, sort_keys=True))