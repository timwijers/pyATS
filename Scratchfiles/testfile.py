def linkRouter5toGWandFortiFW(self):
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
    R5InterfacesUrl = self.AllNodesUrl + '/6/interfaces'
    R5andFWBridgeUrl = self.AllNetworksUrl + '/2'
    FortiGateInterfacesUrl = self.AllNodesUrl + '/5/interfaces'

    R5FormBridgeReq = self.session.post(self.AllNetworksUrl, None, R5FormBridgeData)
    LinkR5ToGwReq = self.session.put(R5InterfacesUrl, LinkR5ToGwData)
    FWtoR5Req = self.session.put(FortiGateInterfacesUrl, FWtoR5andViceVersaData)
    R5toFWReq = self.session.put(R5InterfacesUrl, FWtoR5andViceVersaData)
    R5andFWBridgeVisibilityReq = self.session.put(R5andFWBridgeUrl, R5andFWBridgeVisibilityData)

    return "Link R5 to Gateway status : ", LinkR5ToGwReq.json(), "Form Bridge R5 and FW status : ", \
           R5FormBridgeReq.json(), "Link Firewall to R5 status : ", FWtoR5Req.json(), "Link R5 to Firewall status : ", \
           R5toFWReq.json(), "Hide Bridge between R5 and Firewall status : ", R5andFWBridgeVisibilityReq.json()



def linkVPC123toRouter6(self):
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

        R5InterfacesUrl = self.AllNodesUrl + '/6/interfaces'

        R5andVPCSBridgeVisibilityData = '{"visibility": 0}'

        R5andVPC1BridgeUrl = self.AllNetworksUrl + '/3'
        R5andVPC2BridgeUrl = self.AllNetworksUrl + '/4'
        R5andVPC3BridgeUrl = self.AllNetworksUrl + '/5'

        VPC1InterfacesUrl = self.AllNodesUrl + '/7/interfaces'
        VPC2InterfacesUrl = self.AllNodesUrl + '/8/interfaces'
        VPC3InterfacesUrl = self.AllNodesUrl + '/9/interfaces'

        VPC1FormBridgeReq = self.session.post(self.AllNetworksUrl, None, VPC1FormBridgeData)
        VPC2FormBridgeReq = self.session.post(self.AllNetworksUrl, None, VPC2FormBridgeData)
        VPC3FormBridgeReq = self.session.post(self.AllNetworksUrl, None, VPC3FormBridgeData)

        R5toVPC1Req = self.session.put(R5InterfacesUrl, R5toVPC1Data)
        R5toVPC2Req = self.session.put(R5InterfacesUrl, R5toVPC2Data)
        R5toVPC3Req = self.session.put(R5InterfacesUrl, R5toVPC3Data)

        VPC1ToR5Req = self.session.put(VPC1InterfacesUrl, VPC1toR5Data)
        VPC2ToR5Req = self.session.put(VPC2InterfacesUrl, VPC2toR5Data)
        VPC3ToR5Req = self.session.put(VPC3InterfacesUrl, VPC3toR5Data)

        R5andVPC1BridgeVisibilityReq = self.session.put(R5andVPC1BridgeUrl, R5andVPCSBridgeVisibilityData)
        R5andVPC2BridgeVisibilityReq = self.session.put(R5andVPC2BridgeUrl, R5andVPCSBridgeVisibilityData)
        R5andVPC3BridgeVisibilityReq = self.session.put(R5andVPC3BridgeUrl, R5andVPCSBridgeVisibilityData)

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
