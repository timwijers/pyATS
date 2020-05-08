from pyats.topology import loader
tb = loader.load('routerIOL_tb.yaml')
dev = tb.devices['router1']
devxe = tb.devices['routerXE']
dev.connect(alias='uut', via='cli')
devxe.connect(alias='uutxe', via='netconf')
print(dev.uut.connected)
print(devxe.uutxe.connected)