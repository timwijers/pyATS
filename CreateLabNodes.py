__Author__ = 'Tim Wijers'
__Copyright__ = 'Routz B.V'
__Date__ = 'May 2020'

import requests
import datetime


class CreateLabNodesClass:

    # variables #
    date_time = datetime.datetime.now()
    timestamp = date_time.strftime("%d%m%Y%H%M%S")
    testLabName = 'PyATS_TestLab_' + timestamp
    apiBaseUrl = 'http://10.100.244.1/api'
    labsAuthor = '//Tim%20Wijers/'
    labsFolder = 'pyATS_TestLabs/'

    # Uri's #
    AllLabsUrl = apiBaseUrl + '/labs'
    PyATSTestLabUrl = AllLabsUrl + labsAuthor + labsFolder + testLabName + '.unl'
    AllNodesUrl = PyATSTestLabUrl + '/nodes'
    AllNetworksUrl = PyATSTestLabUrl + '/networks'

    # start session #
    session = requests.Session()

    def login(self):
        """Login to Eve-NG """

        LoginData = '{"username":"tim_wijers","password":"Welkom01"}'
        LoginUrl = self.apiBaseUrl + '/auth/login'
        loginReq = self.session.post(LoginUrl, LoginData)
        return loginReq.json()

    def wipeNodes(self):
        """Stop and Wipe all nodes from previous run """

        NodesStopReq = self.session.get(self.AllNodesUrl + '/stop')
        NodesWipeReq = self.session.get(self.AllNodesUrl + '/wipe')
        return NodesStopReq.json(), NodesWipeReq.json()

    def deleteLab(self):
        """Delete Lab from previous run"""
        LabDelReq = self.session.delete(self.AllLabsUrl + self.labsAuthor + self.labsFolder + self.testLabName + '.unl')
        return LabDelReq.json()

    ### CREATING ###

    def createLab(self):
        """Create New Testlab in the pyATS_TestLabs folder """

        LabConfigData = {
            "path": "/Tim Wijers/pyATS_TestLabs/",
            "name": self.testLabName,
            "version": "1",
            "author": "Tim Wijers",
            "description": "pyATS Test Lab ",
            "body": "This is a testlab created by the Eve-NG REST API. Intended for pyATS framework testing purposes"
        }

        LabConfigReq = self.session.post(self.AllLabsUrl, None, LabConfigData)
        return LabConfigReq.json()

    def createIOLRouter(self, name, positionFromLeft, positionFromTop, nrsOfEthernets, nrsOfSerial):
        """Add Cisco IOL Routers to the lab """

        Node1AddData = {
            "type": "iol",
            "template": "iol",
            "config": "Unconfigured",
            "delay": 0,
            "icon": "Router.png",
            "image": "i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin",
            "name": name,
            "left": positionFromLeft + "%",
            "top": positionFromTop + "%",
            "ram": "1024",
            "cpu": 1,
            "ethernet": nrsOfEthernets,
            "nvram": 1024,
            "serial": nrsOfSerial
        }

        Node1AddReq = self.session.post(self.AllNodesUrl, None, Node1AddData)
        return "Add R1 status : ", Node1AddReq.json()

    def createLinuxNode(self, name, positionFromLeft, positionFromTop, nrsOfEthernets, ramMbs, CPUs, uniqueIdentifier):
        """Add Linux Nodes to the lab """

        LinuxNodeData = {
            "template": "linux",
            "type": "qemu",
            "count": "1",
            "image": "linux-ubuntu-server-18.04-pfne",
            "name": name,
            "icon": "Server.png",
            "uuid": uniqueIdentifier,
            "cpulimit": "undefined",
            "cpu": CPUs,
            "ram": ramMbs,
            "ethernet": nrsOfEthernets,
            "firstmac": "",
            "qemu_version": "",
            "ro_qemu_options": "-machine type=pc,accel=kvm -vga std -usbdevice tablet -boot order=dc",
            "config": "0",
            "delay": "0",
            "console": "vnc",
            "left": positionFromLeft + "%",
            "top": positionFromTop + "%",
            "postfix": 0
        }

        DockerHostAddReq = self.session.post(self.AllNodesUrl, None, LinuxNodeData)
        return "Add Docker Host status : ", DockerHostAddReq.json()

    def createFortiGateNode(self, name, positionFromLeft, positionFromTop, NrsOfEthernets, uniqueIdentifier):
        """Add FortiGate Firewalls to the lab """

        FortiAddData = {
            "template": "fortinet",
            "type": "qemu",
            "count": "1",
            "image": "fortinet-FGT-v6-build0932",
            "name": name,
            "icon": "Firewall.png",
            "uuid": uniqueIdentifier,
            "cpulimit": "undefined",
            "cpu": "1",
            "ram": "1024",
            "ethernet": NrsOfEthernets,
            "qemu_version": "",
            "qemu_arch": "",
            "ro_qemu_options": "-machine type=pc-1.0,accel=kvm -serial mon:stdio -nographic -nodefconfig -nodefaults "
                               "-display none -vga std -rtc base=utc",
            "config": "0",
            "delay": "0",
            "console": "vnc",
            "left": positionFromLeft + "%",
            "top": positionFromTop + "%",
            "postfix": 0
        }

        FortAddReq = self.session.post(self.AllNodesUrl, None, FortiAddData)
        return "Add Fortigate status : ", FortAddReq.json()

    def createVPCs(self, name, positionFromLeft, positionFromTop, numberOfVPCs):
        """Add Virtual PC's to the lab """

        VPCAddData = {
            "template": "vpcs",
            "type": "vpcs",
            "count": "3",
            "name": name,
            "icon": "Desktop.png",
            "config": "0",
            "delay": "0",
            "left": positionFromLeft + "%",
            "top": positionFromTop + "%",
            "postfix": 1,
            "numberNodes": numberOfVPCs
        }

        VPCAddReq = self.session.post(self.AllNodesUrl, None, VPCAddData)
        return "Add VPC's status : ", VPCAddReq.json()

    def createInternetGW(self):
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

        NetworkAddReq = self.session.post(self.AllNetworksUrl, None, NetworkAddData)
        return "Add Internet Gateway network status : ", NetworkAddReq.json()

    ### LINKING ###

    def linkNodeToGW(self, nodeNr):
        """ Link a Node to the Internet Gateway """

        LinkNodeToGwData = '{"0":"1"}'
        NodeInterfacesUrl = self.AllNodesUrl + '/' + nodeNr + '/interfaces'
        LinkNodeToGwReq = self.session.put(NodeInterfacesUrl, LinkNodeToGwData)
        return "Link Node Nr. " + nodeNr + " to Gateway status : ", LinkNodeToGwReq.json(),

    def linkNodeToOtherNodeSerial(self, dataRoutertoRouterLink, nodeNr):
        """ Link Node to Another Node """

        NodeInterfacesUrl = self.AllNodesUrl + '/' + nodeNr + '/interfaces'
        LinkNodeToNodeReq = self.session.put(NodeInterfacesUrl, dataRoutertoRouterLink)
        return "Link Node Nr. " + nodeNr + " to other Node status : ", LinkNodeToNodeReq.json()

    def linkNodeToOtherNodeEthernet(self, bridgeName, portToPortConnectionData_XNode, portToPortConnectionData_YNode, nodeXnr, nodeYnr, bridgeId):

        # First a bridge must be created #
        FormBridgeData = {
            "count": 1,
            "name": bridgeName,
            "type": "bridge",
            "left": 507,
            "top": 241,
            "visibility": 1,
            "postfix": 0
        }

        bridgeVisibilityData = '{"visibility": 0}'

        nodeXinterfacesUrl = self.AllNodesUrl + '/' + nodeXnr + '/interfaces'
        bridgeUrl = self.AllNetworksUrl + '/' + bridgeId
        nodeYinterfacesUrl = self.AllNodesUrl + '/' + nodeYnr + '/interfaces'

        formBridgeReq = self.session.post(self.AllNetworksUrl, None, FormBridgeData)

        NodeXtoNodeYreq = self.session.put(nodeXinterfacesUrl, portToPortConnectionData_XNode)
        NodeYtoNodeXreq = self.session.put(nodeYinterfacesUrl, portToPortConnectionData_YNode)
        bridgeInvisibleReq = self.session.put(bridgeUrl, bridgeVisibilityData)

        return 'Bridge formation status: ', formBridgeReq.json(), '\n' \
               'Node X to Node Y connection status: ', NodeXtoNodeYreq.json(), '\n' \ 
               'Node X to Node Y connection status: ', NodeYtoNodeXreq.json(), '\n' \ 
               'Bridge Invisibility request status: ', bridgeInvisibleReq.json()

    def startAll(self):
        """ Start all nodes """

        NodesStartReq = self.session.get(self.AllNodesUrl + '/start')
        return NodesStartReq.json()

        session.close()
