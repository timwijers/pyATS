import CreateLabNodes

instclass = CreateLabNodes.CreateLabNodesClass()

print(instclass.login())
print(instclass.wipeNodes())
print(instclass.deleteLab())
print(instclass.createLab())

print(instclass.createInternetGW())

print(instclass.createIOLRouter('routeriol1', 40, 60, 1, 1))
print(instclass.createIOLRouter('routeriol2', 50, 70, 1, 1))
print(instclass.createIOLRouter('routeriol3', 60, 60, 1, 1))
print(instclass.createIOLRouter('routeriol5', 20, 20, 1, 1))
print(instclass.createFortiGateNode('fortigate', 10, 20, 1, 'fortigate'))
print(instclass.createLinuxNode('dockerhost', 80, 60, 1, 4096, 2, 'dockerhost'))
print(instclass.createVPCs('vpc', 30, 10, 3))

print(instclass.linkNodeToOtherNodeSerial('{"2":"2:2"}', 1))
print(instclass.linkNodeToOtherNodeSerial('{"18":"3:18"}', 2))
print(instclass.linkNodeToOtherNodeSerial('{"34":"1:34"}', 3))

print(instclass.linkNodeToGW(1))
print(instclass.linkNodeToGW(2))
print(instclass.linkNodeToGW(3))
print(instclass.linkNodeToGW(4))
print(instclass.linkNodeToGW(5))
print(instclass.linkNodeToGW(6))

print(instclass.linkNodeToOtherNodeEthernet('FortiRIOL5_Bridge', '{"1":"2"}','{"1":"2"}', 5, 4, 2))
print(instclass.linkNodeToOtherNodeEthernet('RIOL5VPC1_Bridge', '{"16":3}','{"0":3}', 4, 7, 3))
print(instclass.linkNodeToOtherNodeEthernet('RIOL5VPC2_Bridge', '{"32":4}','{"0":4}', 4, 8, 4))
print(instclass.linkNodeToOtherNodeEthernet('RIOL5VPC3_Bridge', '{"48":5}','{"0":5}', 4, 9, 5))

print(instclass.startAll())