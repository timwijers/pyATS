import requests
import custom_error

loginCreds = {"username":"tim_wijers","password":"Welkom01"}
login = requests.get('http://10.100.244.1/api/auth/login', params=loginCreds)

if login.status_code != 200:
    raise custom_error.APIError('GET /tasks/ {}'.format(login.status_code))
for todo_item in login.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))