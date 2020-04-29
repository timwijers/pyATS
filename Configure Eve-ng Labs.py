import requests
import custom_error

data = '{"username":"admin","password":"eve"}'
url = 'http://10.100.244.1/api/auth/login'
login = requests.post(url,data)

if login.status_code != 200:
    print('status not 200')
    print(login.json())
