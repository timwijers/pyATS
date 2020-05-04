# Uri's #
AllLabsUrl = 'http://10.100.244.1/api/labs'
PyATSTestLabUrl = 'http://10.100.244.1/api/labs//Tim%20Wijers/pyATS_TestLabs/pyATSTestLab.unl'
AllNodesUrl = 'http://10.100.244.1/api/labs/Tim Wijers/pyATS_TestLabs/pyATSTestLab.unl/nodes'
AllNetworksUrl = 'http://10.100.244.1/api/labs/Tim Wijers/pyATS_TestLabs/pyATSTestLab.unl/networks'

# Stop all nodes from previous run #
NodesStopReq = AllNodesUrl + '/stop'

print(NodesStopReq)