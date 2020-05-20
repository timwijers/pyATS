import CreateLabNodes

instclass = CreateLabNodes.CreateLabNodesClass()


print(instclass.login())
print(instclass.wipeNodes())
print(instclass.deleteLab())
print(instclass.createLab())
print(instclass.createRouter1())
print(instclass.createRouter2())
print(instclass.createRouter3())
print(instclass.createDockerHost())
print(instclass.createFortiGate())
print(instclass.createRouter5())
print(instclass.createVPCs())
print(instclass.createInternetGW())
print(instclass.linkRouter123toGW())
print(instclass.linkDockerHosttoGW())
print(instclass.linkFortiFWtoGW())
print(instclass.linkRouter5toGWandFortiFW())
print(instclass.linkVPC123toRouter6())
print(instclass.startAll())

