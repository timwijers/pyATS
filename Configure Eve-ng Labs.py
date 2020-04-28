import requests
import custom_error

payload = {'username': 'tim_wijers', 'password': 'Welkom01'}
url = 'http://10.100.244.1/api/auth/login'
login = requests.post(url, payload)

if login.status_code != 200:
    print('status not 200')
    print(login.json())
