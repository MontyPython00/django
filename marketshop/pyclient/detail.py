import requests 
from getpass import getpass


# endpoint='http://localhost:8000/api/coins/auth/'
# password=getpass()
# data={
#     'username':'admin',
#     'password':password
# }
# auth_response= requests.post(endpoint, json=data)



# if auth_response.status_code == 200:
#     token= auth_response.json()['token']
#     headers={
#         'Authorization': f'Token {token}'
#     }
#     endpoint='http://localhost:8000/api/coins/1/'

#     response= requests.get(endpoint, headers=headers)
#     print(response.json())


endpoint='http://localhost:8000/api/coins/1/'

response= requests.get(endpoint)
print(response.json())