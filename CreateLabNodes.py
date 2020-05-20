__Author__ = 'Tim Wijers'
__Copyright__ = 'Routz B.V'
__Date__ = 'May 2020'

import requests
import datetime

# variables #
date_time = datetime.datetime.now()
timestamp = date_time.strftime("%d%m%Y%H%M%S")
testLabName = 'PyATS_TestLab_' + timestamp
apiBaseUrl = 'http://10.100.244.1/api'
labsAuthor = '//Tim%20Wijers/'
labsFolder = 'pyATS_TestLabs/'

# start session #
session = requests.Session()

# Uri's #
AllLabsUrl = apiBaseUrl + '/labs'
PyATSTestLabUrl = AllLabsUrl + labsAuthor + labsFolder + testLabName + '.unl'
print(PyATSTestLabUrl)
AllNodesUrl = PyATSTestLabUrl + '/nodes'
print(AllNodesUrl)
AllNetworksUrl = PyATSTestLabUrl + '/networks'
print(AllNetworksUrl)


def login():
    """Login to Eve-NG """

    LoginData = '{"username":"tim_wijers","password":"Welkom01"}'
    LoginUrl = apiBaseUrl + '/auth/login'
    loginReq = session.post(LoginUrl, LoginData)
    return loginReq.json()


def wipeNodes():
    """Stop and Wipe all nodes from previous run """

    NodesStopReq = session.get(AllNodesUrl + '/stop')
    NodesWipeReq = session.get(AllNodesUrl + '/wipe')
    return NodesStopReq.json(), NodesWipeReq.json()


def deleteLab():
    """Delete Lab from previous run"""
    LabDelReq = session.delete(AllLabsUrl + labsAuthor + labsFolder + testLabName + '.unl')
    return LabDelReq.json()


### CREATING ###

def createLab():
    """Create New Testlab in the pyATS_TestLabs folder """

    DateTimeObj = datetime.datetime.now()
    LabConfigData = {
        "path": "/Tim Wijers/pyATS_TestLabs/",
        "name": testLabName,
        "version": "1",
        "author": "Tim Wijers",
        "description": "pyATS Test Lab ",
        "body": "This is a testlab created by the Eve-NG REST API. Intended for pyATS framework testing purposes"
    }

    LabConfigReq = session.post(AllLabsUrl, None, LabConfigData)
    return LabConfigReq.json()


def createRouter1():
    """Add router 1 to the lab """

    Node1AddData = {
        "type": "iol",
        "template": "iol",
        "config": "Unconfigured",
        "delay": 0,
        "icon": "Router.png",
        "image": "i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin",
        "name": "pyats_Router1",
        "left": "65%",
        "top": "75%",
        "ram": "1024",
        "cpu": 1,
        "ethernet": 2,
        "nvram": 1024,
        "serial": 1
    }

    Node1AddReq = session.post(AllNodesUrl, None, Node1AddData)
    return "Add R1 status : ", Node1AddReq.json()


def createRouter2():
    """Add router 2 to the lab """

    Node2AddData = {
        "type": "iol",
        "template": "iol",
        "config": "Unconfigured",
        "delay": 0,
        "icon": "Router.png",
        "image": "i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin",
        "name": "pyats_Router2", "left": "35%",
        "top": "95%",
        "ram": "1024",
        "cpu": 1,
        "ethernet": 2,
        "nvram": 1024,
        "serial": 1
    }

    Node2AddReq = session.post(AllNodesUrl, None, Node2AddData)
    return "Add R2 status : ", Node2AddReq.json()


def createRouter3():
    """Add router 3 to the lab """

    Node3AddData = {
        "type": "iol",
        "template": "iol",
        "config": "Unconfigured",
        "delay": 0,
        "icon": "Router.png",
        "image": "i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin",
        "name": "pyats_Router3",
        "left": "95%",
        "top": "95%",
        "ram": "1024",
        "cpu": 1,
        "ethernet": 2,
        "nvram": 1024,
        "serial": 1
    }

    Node3AddReq = session.post(AllNodesUrl, None, Node3AddData)
    return "Add R3 status : ", Node3AddReq.json()


def createDockerHost():
    """Add Docker Host to the lab """

    DockerHostAddData = {
        "template": "linux",
        "type": "qemu",
        "count": "1",
        "image": "linux-ubuntu-server-18.04-pfne",
        "name": "DockerHost",
        "icon": "Server.png",
        "uuid": "",
        "cpulimit": "undefined",
        "cpu": "1",
        "ram": "4096",
        "ethernet": "1",
        "firstmac": "",
        "qemu_version": "",
        "ro_qemu_options": "-machine type=pc,accel=kvm -vga std -usbdevice tablet -boot order=dc",
        "config": "0",
        "delay": "0",
        "console": "vnc",
        "left": "95%",
        "top": "45%",
        "postfix": 0
    }

    DockerHostAddReq = session.post(AllNodesUrl, None, DockerHostAddData)
    return "Add Docker Host status : ", DockerHostAddReq.json()


def createFortiGate():
    """Add FortiGate Firewall to the lab """

    FortiAddData = {
        "template": "fortinet",
        "type": "qemu",
        "count": "1",
        "image": "fortinet-FGT-v6-build0932",
        "name": "FortiGate",
        "icon": "Firewall.png",
        "uuid": "",
        "cpulimit": "undefined",
        "cpu": "1",
        "ram": "1024",
        "ethernet": "4",
        "qemu_version": "",
        "qemu_arch": "",
        "ro_qemu_options": "-machine type=pc-1.0,accel=kvm -serial mon:stdio -nographic -nodefconfig -nodefaults "
                           "-display none -vga std -rtc base=utc",
        "config": "0",
        "delay": "0",
        "console": "vnc",
        "left": "35%",
        "top": "45%",
        "postfix": 0
    }

    FortAddReq = session.post(AllNodesUrl, None, FortiAddData)
    return "Add Fortigate status : ", FortAddReq.json()


def createRouter5():
    """Add Router 5 to the lab """

    NodeAddData = {
        "type": "iol",
        "template": "iol",
        "config": "Unconfigured",
        "delay": 0,
        "icon": "Router.png",
        "image": "i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin",
        "name": "pyats_Router5_behindFW",
        "left": "50%",
        "top": "25%",
        "ram": "1024",
        "cpu": 1,
        "ethernet": 2,
        "nvram": 1024,
        "serial": 1
    }

    NodeAddReq = session.post(AllNodesUrl, None, NodeAddData)
    return "Add R5 status : ", NodeAddReq.json()


def createVPCs():
    """Add Virtual PC's to the lab """

    VPCAddData = {
        "template": "vpcs",
        "type": "vpcs",
        "count": "3",
        "name": "VPC_pyATS",
        "icon": "Desktop.png",
        "config": "0",
        "delay": "0",
        "left": "386",
        "top": "64",
        "postfix": 1,
        "numberNodes": "3"
    }

    VPCAddReq = session.post(AllNodesUrl, None, VPCAddData)
    return "Add VPC's status : ", VPCAddReq.json()


def createDockerHost():
    """ Create a new Internet Gateway for internet connection """

    NetworkAddData = {
        "count": "1",
        "visibility": "1",
        "name": "InternetGW",
        "type": "pnet0",
        "left": "65%",
        "top": "45%",
        "postfix": 0
    }

    NetworkAddReq = session.post(AllNetworksUrl, None, NetworkAddData)
    return "Add Internet Gateway network status : ", NetworkAddReq.json()


### LINKING ###

def linkRouter123toGW():
    """ Link Router 1, 2 and 3 to the Internet Gateway via ethernet """

    LinkR1ToGwData = '{"0":"1"}'
    LinkR1ToR2Data = '{"2":"2:2"}'
    R1InterfacesUrl = AllNodesUrl + '/1/interfaces'
    LinkR1ToGwReq = session.put(R1InterfacesUrl, LinkR1ToGwData)
    LinkR1ToR2Req = session.put(R1InterfacesUrl, LinkR1ToR2Data)

    LinkR2ToGwData = '{"0":"1"}'
    LinkR2ToR3Data = '{"18":"3:18"}'
    R2InterfacesUrl = AllNodesUrl + '/2/interfaces'
    LinkR2ToGwReq = session.put(R2InterfacesUrl, LinkR2ToGwData)
    LinkR2ToR3Req = session.put(R2InterfacesUrl, LinkR2ToR3Data)

    LinkR3ToGwData = '{"0":"1"}'
    LinkR3ToR1Data = '{"34":"1:34"}'
    R3InterfacesUrl = AllNodesUrl + '/3/interfaces'
    LinkR3ToGwReq = session.put(R3InterfacesUrl, LinkR3ToGwData)
    LinkR3ToR1Req = session.put(R3InterfacesUrl, LinkR3ToR1Data)

    return "Link R1 to Gateway status : ", LinkR1ToGwReq.json(), "Link R1 to R2 status : ", LinkR1ToR2Req.json(), \
           "Link R2 to Gateway status : ", LinkR2ToGwReq.json(), "Link R2 to R3 status : ", LinkR2ToR3Req.json(), \
           "Link R3 to Gateway status : ", LinkR3ToGwReq.json(), "Link R3 to R1 status : ", LinkR3ToR1Req.json()


def linkDockerHosttoGW():
    """ Link the Docker Host to the gateway via Ethernet """

    LinkDockerHostToGwData = '{"0":"1"}'
    DockerHostInterfacesUrl = AllNodesUrl + '/4/interfaces'
    LinkDockerHostToGwReq = session.put(DockerHostInterfacesUrl, LinkDockerHostToGwData)
    return "Link Docker Host to Gateway status : ", LinkDockerHostToGwReq.json()


def linkFortiFWtoGW():
    """ Link the FortiGate Firewall to the gateway via Ethernet """

    LinkFortiGateToGwData = '{"0":"1"}'
    FortiGateInterfacesUrl = AllNodesUrl + '/5/interfaces'
    LinkFortiGateToGwReq = session.put(FortiGateInterfacesUrl, LinkFortiGateToGwData)
    return "Link Fortigate to Gateway status : ", LinkFortiGateToGwReq.json()


def linkRouter5toGWandFortiFW():
    """ Link Router 5 to the gateway and the Fortigate Firewall via Ethernet """

    R5FormBridgeData = {
        "count": 1,
        "name": "Net-pyats_Router5_behindFWiface_16",
        "type": "bridge",
        "left": 507,
        "top": 241,
        "visibility": 1,
        "postfix": 0
    }

    LinkR5ToGwData = '{"0":"1"}'
    R5andFWBridgeVisibilityData = '{"visibility": 0}'
    FWtoR5andViceVersaData = '{"1":"2"}'
    R5InterfacesUrl = AllNodesUrl + '/6/interfaces'
    R5andFWBridgeUrl = AllNetworksUrl + '/2'
    FortiGateInterfacesUrl = AllNodesUrl + '/5/interfaces'

    R5FormBridgeReq = session.post(AllNetworksUrl, None, R5FormBridgeData)
    LinkR5ToGwReq = session.put(R5InterfacesUrl, LinkR5ToGwData)
    FWtoR5Req = session.put(FortiGateInterfacesUrl, FWtoR5andViceVersaData)
    R5toFWReq = session.put(R5InterfacesUrl, FWtoR5andViceVersaData)
    R5andFWBridgeVisibilityReq = session.put(R5andFWBridgeUrl, R5andFWBridgeVisibilityData)

    return "Link R5 to Gateway status : ", LinkR5ToGwReq.json(), "Form Bridge R5 and FW status : ", \
           R5FormBridgeReq.json(), "Link Firewall to R5 status : ", FWtoR5Req.json(), "Link R5 to Firewall status : ", \
           R5toFWReq.json(), "Hide Bridge between R5 and Firewall status : ", R5andFWBridgeVisibilityReq.json()


def linkVPC123toRouter6():
    """ Link VPC 1,2 and 3 to Router 6 """

    VPC1FormBridgeData = {
        "count": 1,
        "name": "Net-VPC1iface_0",
        "type": "bridge",
        "left": 566,
        "top": 104,
        "visibility": 1,
        "postfix": 0
    }
    VPC2FormBridgeData = {
        "count": 1,
        "name": "Net-VPC2iface_0",
        "type": "bridge",
        "left": 506,
        "top": 104,
        "visibility": 1,
        "postfix": 0
    }
    VPC3FormBridgeData = {
        "count": 1,
        "name": "Net-VPC3iface_0",
        "type": "bridge",
        "left": 446,
        "top": 104,
        "visibility": 1,
        "postfix": 0
    }

    R5toVPC1Data = '{"16":3}'
    R5toVPC2Data = '{"32":4}'
    R5toVPC3Data = '{"48":5}'

    VPC1toR5Data = '{"0":3}'
    VPC2toR5Data = '{"0":4}'
    VPC3toR5Data = '{"0":5}'

    R5InterfacesUrl = AllNodesUrl + '/6/interfaces'

    R5andVPCSBridgeVisibilityData = '{"visibility": 0}'

    R5andVPC1BridgeUrl = AllNetworksUrl + '/3'
    R5andVPC2BridgeUrl = AllNetworksUrl + '/4'
    R5andVPC3BridgeUrl = AllNetworksUrl + '/5'

    VPC1InterfacesUrl = AllNodesUrl + '/7/interfaces'
    VPC2InterfacesUrl = AllNodesUrl + '/8/interfaces'
    VPC3InterfacesUrl = AllNodesUrl + '/9/interfaces'

    VPC1FormBridgeReq = session.post(AllNetworksUrl, None, VPC1FormBridgeData)
    VPC2FormBridgeReq = session.post(AllNetworksUrl, None, VPC2FormBridgeData)
    VPC3FormBridgeReq = session.post(AllNetworksUrl, None, VPC3FormBridgeData)

    R5toVPC1Req = session.put(R5InterfacesUrl, R5toVPC1Data)
    R5toVPC2Req = session.put(R5InterfacesUrl, R5toVPC2Data)
    R5toVPC3Req = session.put(R5InterfacesUrl, R5toVPC3Data)

    VPC1ToR5Req = session.put(VPC1InterfacesUrl, VPC1toR5Data)
    VPC2ToR5Req = session.put(VPC2InterfacesUrl, VPC2toR5Data)
    VPC3ToR5Req = session.put(VPC3InterfacesUrl, VPC3toR5Data)

    R5andVPC1BridgeVisibilityReq = session.put(R5andVPC1BridgeUrl, R5andVPCSBridgeVisibilityData)
    R5andVPC2BridgeVisibilityReq = session.put(R5andVPC2BridgeUrl, R5andVPCSBridgeVisibilityData)
    R5andVPC3BridgeVisibilityReq = session.put(R5andVPC3BridgeUrl, R5andVPCSBridgeVisibilityData)

    return "Form Bridge R5 and VPC1 status : ", VPC1FormBridgeReq.json(), \
           "Form Bridge R5 and VPC2 status : ", VPC2FormBridgeReq.json(), \
           "Form Bridge R5 and VPC3 status : ", VPC3FormBridgeReq.json(), \
           "Link R5 to VPC 1 status : ", R5toVPC1Req.json(), \
           "Link R5 to VPC 2 status : ", R5toVPC2Req.json(), \
           "Link R5 to VPC 3 status : ", R5toVPC3Req.json(), \
           "Link VPC 1 to R5 status : ", VPC1ToR5Req.json(), \
           "Link VPC 2 to R5 status : ", VPC2ToR5Req.json(), \
           "Link VPC 3 to R5 status : ", VPC3ToR5Req.json(), \
           "Hide Bridge between R5 and VPC 1 status : ", R5andVPC1BridgeVisibilityReq.json(), \
           "Hide Bridge between R5 and VPC 2 status : ", R5andVPC2BridgeVisibilityReq.json(), \
           "Hide Bridge between R5 and VPC 3 status : ", R5andVPC3BridgeVisibilityReq.json(),


def startAll():
    """ Start all nodes """

    NodesStartReq = session.get(AllNodesUrl + '/start')
    return NodesStartReq.json()


# Close REST API session #
session.close()


class CreateLabNodesClass:
    pass
