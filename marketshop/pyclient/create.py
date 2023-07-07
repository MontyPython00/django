import requests
from getpass import getpass

endpoint='http://localhost:8000/api/coins/auth/'
password=getpass()
data={
      'username':'staff',
      'password':password
}

auth_response= requests.post(endpoint, data=data)


if auth_response.status_code==200:
      token= auth_response.json()['token']
      headers={
            'Authorization': f'Token {token}'
      }
      endpoint='http://localhost:8000/api/coins/'

      data={
            'name':'AnotherPyClientAPI',
            'description':'TestDescriptionWithTokenAuthorization',
            'price':13}

      response= requests.post(endpoint, headers=headers, json=data)

      print(response.json())
      