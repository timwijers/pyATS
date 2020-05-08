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

### CREATING ###

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

# Add Docker Host to the lab #
DockerHostAddData = '{"template":"linux","type":"qemu","count":"1","image":"linux-ubuntu-server-18.04-pfne",' \
                    '"name":"DockerHost","icon":"Server.png","uuid":"","cpulimit":"undefined","cpu":"1","ram":"4096",' \
                    '"ethernet":"1","firstmac":"","qemu_version": "","ro_qemu_options":"-machine type=pc,accel=kvm ' \
                    '-vga std -usbdevice tablet -boot ' \
                    'order=dc","config":"0","delay":"0","console":"vnc","left":"95%","top":"45%","postfix":0} '
DockerHostAddReq = session.post(AllNodesUrl, DockerHostAddData)
print(DockerHostAddReq.json())

# Add FortiGate Firewall to the lab #
FortiAddData = '{"template":"fortinet","type":"qemu","count":"1","image":"fortinet-FGT-v6-build0932",' \
               '"name":"FortiGate","icon":"Firewall.png","uuid":"","cpulimit":"undefined","cpu":"1","ram":"1024",' \
               '"ethernet":"4","qemu_version":"","qemu_arch":"","ro_qemu_options":"-machine type=pc-1.0,accel=kvm ' \
               '-serial mon:stdio -nographic -nodefconfig -nodefaults -display none -vga std -rtc base=utc",' \
               '"config":"0","delay":"0","console":"vnc","left":"35%","top":"45%","postfix":0} '
FortAddReq = session.post(AllNodesUrl, FortiAddData)
print(FortAddReq.json())

# Add router 5 to the lab #
NodeAddData = '{"type":"iol","template":"iol","config":"Unconfigured","delay":0,"icon":"Router.png",' \
              '"image":"i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin","name":"pyats_Router5_behindFW",' \
              '"left":"50%","top":"25%","ram":"1024","cpu":1,"ethernet":2, "nvram": 1024, "serial": 1} '

NodeAddReq = session.post(AllNodesUrl, NodeAddData)
print(NodeAddReq.json())

VPCAddData = '{"template":"vpcs","type":"vpcs","count":"3","name":"VPC_pyATS","icon":"Desktop.png","config":"0",' \
             '"delay":"0","left":"386","top":"64","postfix":1,"numberNodes":"3"} '
VPCAddReq = session.post(AllNodesUrl, VPCAddData)
print(VPCAddReq.json())

# Create a new Internet Gateway for internet connection #
NetworkAddData = '{"count":"1","visibility":"1","name":"InternetGW","type":"pnet0","left":"65%","top":"45%",' \
                 '"postfix":0} '
NetworkAddReq = session.post(AllNetworksUrl, NetworkAddData)
print(NetworkAddReq.json())

VPC1FormBridgeData = '{"count":1,"name":"Net-VPC1iface_0","type":"bridge","left":566,"top":104,"visibility":1,' \
                     '"postfix":0} '
VPC2FormBridgeData = '{"count":1,"name":"Net-VPC2iface_0","type":"bridge","left":506,"top":104,"visibility":1,' \
                     '"postfix":0} '
VPC3FormBridgeData = '{"count":1,"name":"Net-VPC1iface_0","type":"bridge","left":446,"top":104,"visibility":1,' \
                     '"postfix":0} '

VPC1FormBridgeReq = session.post(AllNetworksUrl, VPC1FormBridgeData)
print(VPC1FormBridgeReq.json())
VPC2FormBridgeReq = session.post(AllNetworksUrl, VPC2FormBridgeData)
print(VPC2FormBridgeReq.json())
VPC3FormBridgeReq = session.post(AllNetworksUrl, VPC3FormBridgeData)
print(VPC3FormBridgeReq.json())

R5FormBridgeData = '{"count":1,"name":"Net-pyats_Router5_behindFWiface_16","type":"bridge","left":507,"top":241,' \
                   '"visibility":1,"postfix":0} '

R5FormBridgeReq = session.post(AllNetworksUrl, R5FormBridgeData)
print(R5FormBridgeReq.json())

### LINKING ###

# Link Router 1, 2 and 3 to the Internet Gateway via ethernet #
LinkR1ToGwData = '{"0":"1"}'
LinkR1ToR2Data = '{"2":"2:2"}'
R1InterfacesUrl = AllNodesUrl + '/1/interfaces'
LinkR1ToGwReq = session.put(R1InterfacesUrl, LinkR1ToGwData)
LinkR1ToR2Req = session.put(R1InterfacesUrl, LinkR1ToR2Data)
print(LinkR1ToGwReq.json())
print(LinkR1ToR2Req.json())

LinkR2ToGwData = '{"0":"1"}'
LinkR2ToR3Data = '{"18":"3:18"}'
R2InterfacesUrl = AllNodesUrl + '/2/interfaces'
LinkR2ToGwReq = session.put(R2InterfacesUrl, LinkR2ToGwData)
LinkR2ToR3Req = session.put(R2InterfacesUrl, LinkR2ToR3Data)
print(LinkR2ToGwReq.json())
print(LinkR2ToR3Req.json())

LinkR3ToGwData = '{"0":"1"}'
LinkR3ToR1Data = '{"34":"1:34"}'
R3InterfacesUrl = AllNodesUrl + '/3/interfaces'
LinkR3ToGwReq = session.put(R3InterfacesUrl, LinkR3ToGwData)
LinkR3ToR1Req = session.put(R3InterfacesUrl, LinkR3ToR1Data)
print(LinkR3ToGwReq.json())
print(LinkR3ToR1Req.json())

# Link the Docker Host to the gateway via Ethernet #
LinkDockerHostToGwData = '{"0":"1"}'
DockerHostInterfacesUrl = AllNodesUrl + '/4/interfaces'
LinkDockerHostToGwReq = session.put(DockerHostInterfacesUrl, LinkDockerHostToGwData)
print(LinkDockerHostToGwReq.json())

# Link the FortiGate Firewall to the gateway via Ethernet #
LinkFortiGateToGwData = '{"0":"1"}'
FortiGateInterfacesUrl = AllNodesUrl + '/5/interfaces'
LinkFortiGateToGwReq = session.put(FortiGateInterfacesUrl, LinkFortiGateToGwData)
print(LinkFortiGateToGwReq.json())

# Link Router 5 to the gateway and the Fortigate Firewall via Ethernet #
LinkR5ToGwData = '{"0":"1"}'
FWtoR5Data = '{"1":"2"}'
R5toFWData = '{"16":"2"}'

R5InterfacesUrl = AllNodesUrl + '/6/interfaces'

LinkR5ToGwReq = session.put(R5InterfacesUrl, LinkR5ToGwData)

FWtoR5Req = session.put(FortiGateInterfacesUrl, FWtoR5Data)
R5toFWReq = session.put(R5InterfacesUrl, R5toFWData)

print(LinkR5ToGwReq.json())

print(FWtoR5Req.json())
print(R5toFWReq.json())

# Link VPC 1,2 and 3 to Router 6 #

R5toVPC1Data = '{"16":3}'
R5toVPC2Data = '{"32":4}'
R5toVPC3Data = '{"48":5}'

VPC1toR5Data = '{"0":3}'
VPC2toR5Data = '{"0":4}'
VPC3toR5Data = '{"0":5}'

VPC1InterfacesUrl = AllNodesUrl + '/7/interfaces'
VPC2InterfacesUrl = AllNodesUrl + '/8/interfaces'
VPC3InterfacesUrl = AllNodesUrl + '/9/interfaces'

R5toVPC1Req = session.put(R5InterfacesUrl, R5toVPC1Data)
R5toVPC1Req = session.put(R5InterfacesUrl, R5toVPC2Data)
R5toVPC1Req = session.put(R5InterfacesUrl, R5toVPC3Data)

VPC1ToR5Req = session.put(VPC1InterfacesUrl, VPC1toR5Data)
VPC2ToR5Req = session.put(VPC2InterfacesUrl, VPC2toR5Data)
VPC3ToR5Req = session.put(VPC3InterfacesUrl, VPC3toR5Data)

# Start all nodes #
NodesStartReq = session.get(AllNodesUrl + '/start')
print(NodesStartReq.json())

# TelNetSession = telnetlib.Telnet('10.100.244.1', 45569)
