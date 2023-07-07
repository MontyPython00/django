import requests
from getpass import getpass, getuser

password=getpass()

endpoint= 'http://localhost:8000/api/coins/auth/'
data= {
    'username':'staff',
    'password':password
}
auth_token=requests.post(endpoint, json=data)



if auth_token.status_code == 200:
    token=auth_token.json()['token']
    headers={
        'Authorization': f'Token {token}'
    }
    endpoint='http://localhost:8000/api/coins/'

    response=requests.get(endpoint, headers=headers)

    print(response.json())
    