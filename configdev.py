# Example
# -------
#
#   connecting to device

# using the sample topology file from
import os
from pyats import topology

testbedfile = os.path.join(os.path.dirname(topology.__file__),
                           'routerIOL_tb.yaml')
testbed = topology.loader.load(testbedfile)

# pick a device

routeriol1 = testbed.devices['routeriol']

routeriol1.connect()
routeriol1.is_connected()
# True
routeriol1.default
routeriol1.default.execute('show ip int brief')
