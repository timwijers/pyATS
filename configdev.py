# Example
# -------
#
#   connecting to device

# using the sample topology file from
import os
from pyats import topology
from genie.testbed import load

testbed = load('routerIOL_tb.yaml')

routeriol1 = testbed.devices['routeriol']
routeriol2 = testbed.devices['routeriol2']

routeriol1.connect()

routeriol2.connect()

routeriol1.configure("interface ethernet0/2\n" " ip address 192.168.3.2 255.255.255.0\n" " no sh\n")
routeriol2.configure("interface ethernet0/2\n" " ip address 192.168.3.3 255.255.255.0\n" " no sh\n")

routeriol1.execute('show ip int brief')
routeriol2.execute('show ip int brief')

routeriol1.parse('show ip interface brief ethernet0/2')
