import requests
import custom_error

loginCreds = {"username":"tim_wijers","password":"Welkom01"}
login = requests.get('http://10.100.244.1/api/auth/login', params=loginCreds)

if login.status_code != 200:
    print('status not 200')

for item in login.json():
    print('{} {}'.format(item['id'], item['summary']))