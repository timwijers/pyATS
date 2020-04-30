import datetime

import requests
import custom_error

# start session #
session = requests.Session()

# Login to Eve-NG #
LoginData = '{"username":"tim_wijers","password":"Welkom01"}'
LoginUrl = 'http://10.100.244.1/api/auth/login'
loginReq = session.post(LoginUrl, LoginData)
print(loginReq.json())

# Create New Testlab in the pyATS_TestLabs folder #
DateTimeObj = datetime.datetime.now()
LabConfigData = '{"path":"/Tim Wijers/pyATS_TestLabs/","name":"pyATSTestLab","version":"1","author":"Tim Wijers",' \
                '"description":"pyATS Test Lab ","body":"This is a testlab created by the Eve-NG REST API. Intended ' \
                'for pyATS framework testing purposes"} '

LabConfigUrl = 'http://10.100.244.1/api/labs'
LabConfigReq = session.post(LabConfigUrl, LabConfigData)
print(LabConfigReq.json())


# Add router 1 to the lab #
NodeAddData = '{"type":"iol","template":"iol","config":"Unconfigured","delay":0,"icon":"Router.png",' \
              '"image":"i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin","name":"pyats_Router1","left":"35%",' \
              '"top":"25%","ram":"1024","cpu":1,"ethernet":2, "nvram": 1024, "serial": 1} '
NodeAddUrl = 'http://10.100.244.1/api/labs/Tim Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes'
NodeAddReq = session.post(NodeAddUrl, NodeAddData)
print(NodeAddReq.json())

# Add router 2 to the lab #
NodeAddData = '{"type":"iol","template":"iol","config":"Unconfigured","delay":0,"icon":"Router.png",' \
              '"image":"i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin","name":"pyats_Router2","left":"35%",' \
              '"top":"25%","ram":"1024","cpu":1,"ethernet":2, "nvram": 1024, "serial": 1} '
NodeAddUrl = 'http://10.100.244.1/api/labs/Tim Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes'
NodeAddReq = session.post(NodeAddUrl, NodeAddData)
print(NodeAddReq.json())

# Add router 3 to the lab #
NodeAddData = '{"type":"iol","template":"iol","config":"Unconfigured","delay":0,"icon":"Router.png",' \
              '"image":"i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin","name":"pyats_Router3","left":"35%",' \
              '"top":"25%","ram":"1024","cpu":1,"ethernet":2, "nvram": 1024, "serial": 1} '
NodeAddUrl = 'http://10.100.244.1/api/labs/Tim Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes'
NodeAddReq = session.post(NodeAddUrl, NodeAddData)
print(NodeAddReq.json())

# Create a new Internet Gateway for internet connection #
NetworkAddData = '{"type":"Management(Cloud0)","name":"InternetGateway","left":"35%","top":"25%"}'
NetworkAddUrl = 'http://10.100.244.1/api/labs/Tim Wijers/pyATS_TestLabs/pyATSTestLab.unl/networks'
NetworkAddReq = session.post(NetworkAddUrl, NetworkAddData)
print(NetworkAddReq.json())


