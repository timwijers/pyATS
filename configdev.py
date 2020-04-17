# Example
# -------
#
#   connecting to device

# using the sample topology file from
import os
from pyats import topology


testbed = topology.loader.load('routerIOL_tb.yaml')

# pick a device

routeriol1 = testbed.devices['routeriol']
routeriol2 = testbed.devices['routeriol2']

routeriol1.connect()
routeriol1.default
routeriol2.connect()
routeriol2.default
routeriol1.default.execute('show ip int brief')
routeriol2.default.execute('show ip int brief')