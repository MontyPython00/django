import requests

endpoint='http://localhost:8000/api/coins/5/delete/'

response= requests.delete(endpoint)

print(response.status_code, response.status_code==204)