import datetime
import requests
date_time = datetime.datetime.now()
timestamp = date_time.strftime("%d%m%Y%H%M%S")

print(timestamp)
session = requests.Session()

LoginData = '{"username":"tim_wijers","password":"Welkom01"}'
LoginUrl = 'http://10.100.244.1/api/auth/login'
print(session.post(LoginUrl,LoginData).json())

Url = 'http://10.100.244.1/api/labs'
Data = {"path":"/Tim%20Wijers/pyATS_TestLabs/","name":"pyats111052021","version":"1",' \
                '"author":"Tim Wijers","description":"pyATS Test Lab ","body":"This is a testlab created by the ' \
                'Eve-NG REST API. Intended for pyATS framework testing purposes"}
print(session.post(Url,Data).json())
