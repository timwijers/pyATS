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

# Delete Lab from previous run #
LabUrl = 'http://10.100.244.1/api/labs//Tim%20Wijers/pyATS_TestLabs/pyATSTestLab.unl'

LabDelReq = session.delete(LabUrl)
print(LabDelReq.json())

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

# Link Router 1, 2 and 3 to the Internet Gateway via ethernet #

LinkToGwData1 = '{"0":"1"}'
LinkToGwUrl1 = 'http://10.100.244.1/api/labs/Tim%20Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes/1/interfaces'
LinkToGwReq1 = session.put(LinkToGwUrl1, LinkToGwData1)
print(LinkToGwReq1.json())

LinkToGwData2 = '{"0":"1"}'
LinkToGwUrl2 = 'http://10.100.244.1/api/labs/Tim%20Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes/2/interfaces'
LinkToGwReq2 = session.put(LinkToGwUrl2, LinkToGwData2)
print(LinkToGwReq2.json())

LinkToGwData3 = '{"0":"1"}'
LinkToGwUrl3 = 'http://10.100.244.1/api/labs/Tim%20Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes/3/interfaces'
LinkToGwReq3 = session.put(LinkToGwUrl3, LinkToGwData3)
print(LinkToGwReq3.json())
