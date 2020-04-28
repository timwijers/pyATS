import requests
import custom_error

loginCreds = {'username': 'tim_wijers', 'password': 'Welkom01'}
login = requests.post('http://10.100.244.1/api/auth/login', data={'username': 'tim_wijers', 'password': 'Welkom01'})

if login.status_code != 200:
    print('status not 200')
    print(login.json())
