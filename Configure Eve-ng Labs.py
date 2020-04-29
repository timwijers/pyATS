import datetime

import requests
import custom_error

# start sesssion #
session = requests.Session()
# Login to Eve-NG #
LoginData = '{"username":"tim_wijers","password":"Welkom01"}'
LoginUrl = 'http://10.100.244.1/api/auth/login'
loginReq = session.post(LoginUrl, LoginData)
print(loginReq.json())

# Create New Testlab in the pyATS_TestLabs folder #
DateTimeObj = datetime.datetime.now()
LabConfigData = '{"path":"/Tim Wijers/pyATS_TestLabs/","name":"pyATSTestLab_2","version":"1","author":"Tim Wijers",' \
                '"description":"pyATS Test Lab_2","body":"This is a testlab created by the Eve-NG REST API. Intended ' \
                'for pyATS framework testing purposes"} '

LabConfigUrl = 'http://10.100.244.1/api/labs'

LabConfigReq = session.post(LabConfigUrl, LabConfigData)
print(LabConfigReq.json())
