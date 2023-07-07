import requests

endpoint='http://localhost:8000/api/coins/market_list'

response= requests.get(endpoint)

print(response.json())