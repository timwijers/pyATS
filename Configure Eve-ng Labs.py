__Author__ = 'Tim Wijers'
__Copyright__ = 'Routz B.V'
__Date__ = 'May 2020'

import datetime
import telnetlib
import requests
import getpass
import custom_error

# start session #
session = requests.Session()

# Login to Eve-NG #
LoginData = '{"username":"tim_wijers","password":"Welkom01"}'
LoginUrl = 'http://10.100.244.1/api/auth/login'
loginReq = session.post(LoginUrl, LoginData)
print(loginReq.json())

# Uri's #
AllLabsUrl = 'http://10.100.244.1/api/labs'
PyATSTestLabUrl = 'http://10.100.244.1/api/labs//Tim%20Wijers/pyATS_TestLabs/pyATSTestLab.unl'
AllNodesUrl = 'http://10.100.244.1/api/labs/Tim Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes'
AllNetworksUrl = 'http://10.100.244.1/api/labs/Tim Wijers/pyATS_TestLabs/pyATSTestLab.unl/networks'

# Stop all nodes from previous run #
NodesStopReq = session.get(AllNodesUrl + '/stop')
print(NodesStopReq.json())

# Delete Lab from previous run #
LabDelReq = session.delete(PyATSTestLabUrl)
print(LabDelReq.json())

# Create New Testlab in the pyATS_TestLabs folder #
DateTimeObj = datetime.datetime.now()
LabConfigData = '{"path":"/Tim Wijers/pyATS_TestLabs/","name":"pyATSTestLab","version":"1","author":"Tim Wijers",' \
                '"description":"pyATS Test Lab ","body":"This is a testlab created by the Eve-NG REST API. Intended ' \
                'for pyATS framework testing purposes"} '

LabConfigReq = session.post(AllLabsUrl, LabConfigData)
print(LabConfigReq.json())

# Add router 1 to the lab #
NodeAddData = '{"type":"iol","template":"iol","config":"Unconfigured","delay":0,"icon":"Router.png",' \
              '"image":"i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin","name":"pyats_Router1","left":"65%",' \
              '"top":"75%","ram":"1024","cpu":1,"ethernet":2, "nvram": 1024, "serial": 1} '
NodeAddReq = session.post(AllNodesUrl, NodeAddData)
print(NodeAddReq.json())

# Add router 2 to the lab #
NodeAddData = '{"type":"iol","template":"iol","config":"Unconfigured","delay":0,"icon":"Router.png",' \
              '"image":"i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin","name":"pyats_Router2","left":"35%",' \
              '"top":"95%","ram":"1024","cpu":1,"ethernet":2, "nvram": 1024, "serial": 1} '

NodeAddReq = session.post(AllNodesUrl, NodeAddData)
print(NodeAddReq.json())

# Add router 3 to the lab #
NodeAddData = '{"type":"iol","template":"iol","config":"Unconfigured","delay":0,"icon":"Router.png",' \
              '"image":"i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin","name":"pyats_Router3","left":"95%",' \
              '"top":"95%","ram":"1024","cpu":1,"ethernet":2, "nvram": 1024, "serial": 1} '
NodeAddReq = session.post(AllNodesUrl, NodeAddData)
print(NodeAddReq.json())

DockerHostAddData = '{"template":"linux","type":"qemu","count":"1","image":"linux-ubuntu-server-18.04-pfne",' \
                    '"name":"DockerHost","icon":"Server.png","uuid":"","cpulimit":"undefined","cpu":"1","ram":"4096",' \
                    '"ethernet":"1","firstmac":"","qemu_version": "","ro_qemu_options":"-machine type=pc,accel=kvm ' \
                    '-vga std -usbdevice tablet -boot ' \
                    'order=dc","config":"0","delay":"0","console":"telnet","left":"85%","top":"45%","postfix":0} '
DockerHostAddReq = session.post(AllNodesUrl, DockerHostAddData)
print(DockerHostAddReq.json())

# Create a new Internet Gateway for internet connection #
NetworkAddData = '{"count":"1","visibility":"1","name":"InternetGW","type":"pnet0","left":"65%","top":"45%",' \
                 '"postfix":0} '
NetworkAddReq = session.post(AllNetworksUrl, NetworkAddData)
print(NetworkAddReq.json())

# Link Router 1, 2 and 3 to the Internet Gateway via ethernet #
LinkR1ToGwData = '{"0":"1"}'
LinkR1ToR2Data = '{"2":"2:2"}'
R1InterfacesUrl = 'http://10.100.244.1/api/labs/Tim%20Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes/1/interfaces'
LinkR1ToGwReq = session.put(R1InterfacesUrl, LinkR1ToGwData)
LinkR1ToR2Req = session.put(R1InterfacesUrl, LinkR1ToR2Data)
print(LinkR1ToGwReq.json())
print(LinkR1ToR2Req.json())

LinkR2ToGwData = '{"0":"1"}'
LinkR2ToR3Data = '{"18":"3:18"}'
R2InterfacesUrl = 'http://10.100.244.1/api/labs/Tim%20Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes/2/interfaces'
LinkR2ToGwReq = session.put(R2InterfacesUrl, LinkR2ToGwData)
LinkR2ToR3Req = session.put(R2InterfacesUrl, LinkR2ToR3Data)
print(LinkR2ToGwReq.json())
print(LinkR2ToR3Req.json())

LinkR3ToGwData = '{"0":"1"}'
LinkR3ToR1Data = '{"34":"1:34"}'
R3InterfacesUrl = 'http://10.100.244.1/api/labs/Tim%20Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes/3/interfaces'
LinkR3ToGwReq = session.put(R3InterfacesUrl, LinkR3ToGwData)
LinkR3ToR1Req = session.put(R3InterfacesUrl, LinkR3ToR1Data)
print(LinkR3ToGwReq.json())
print(LinkR3ToR1Req.json())

LinkDockerHostToGwData = '{"0":"1"}'
DockerHostInterfacesUrl = 'http://10.100.244.1/api/labs/Tim%20Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes/4/interfaces'
LinkDockerHostToGwReq = session.put(DockerHostInterfacesUrl, LinkDockerHostToGwData)
print(LinkDockerHostToGwReq.json())

# Start all nodes #
NodesStartReq = session.get(AllNodesUrl + '/start')
print(NodesStartReq.json())

# TelNetSession = telnetlib.Telnet('10.100.244.1', 45569)
