import requests

endpoint= 'http://localhost:8000/api/coins/1/update/'

data={
    'name':'bitcoin',
    'description':'Coin',
}

response= requests.patch(endpoint, json=data)
print(response.json())