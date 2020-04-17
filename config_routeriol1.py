# Python imports
import os
import time
import logging

# pyATS import
from pyats import aetest
from pyats import topology
from genie.harness.base import Trigger
from genie.testbed import load

log = logging.getLogger()


### setup actions ###
class common_setup(aetest.CommonSetup):
    """ Common Setup section """

    # CommonSetup have subsection.
    # You can have 1 to as many subsection as wanted

    # First subsection
    @aetest.subsection
    def connect(self, testscript, testbed):
        """ Common Setup subsection """
        log.info("Aetest Common Setup ")

        testbed = load('routerIOL_tb.yaml')
        routeriol1 = testbed.devices['routeriol']
        routeriol2 = testbed.devices['routeriol2']

        routeriol1.connect()
        routeriol2.connect()

        testscript.parameters['uut'] = routeriol1
        testscript.parameters['uut2'] = routeriol2


### test cases ###
class test_cases(aetest.Testcase):
    """ This is user Testcases section """

    @aetest.setup
    def configure_devices(self, section, uut, uut2):
        """ Testcase Setup section """
        log.info("Preparing the test")
        log.info(section)

        uut.configure("interface ethernet0/1\n" " ip address 192.168.2.2 255.255.255.0\n" " no sh\n")
        uut2.configure("interface ethernet0/1\n" " ip address 192.168.2.3 255.255.255.0\n" " no sh\n")

        uut.configure("interface ethernet0/2\n" " ip address 192.168.3.2 255.255.255.0\n" " no sh\n")
        uut2.configure("interface ethernet0/2\n" " ip address 192.168.3.3 255.255.255.0\n" " no sh\n")

    @aetest.test
    def check_interface2_not_down_routeriol1(self, uut):
        var = uut.parse('show ip interface brief ethernet0/2')
        if var['interface']['Ethernet0/2']['status'] != 'up': self.failed('interface ethernet0/2 is not up')

    @aetest.test
    def check_interface2_not_down_routeriol2(self, uut2):
        var = uut2.parse('show ip interface brief ethernet0/2')
        if var['interface']['Ethernet0/2']['status'] != 'up': self.failed('interface ethernet0/2 is not up')

    @aetest.test
    def check_ip_correct_routeriol1(self, uut):
        var = uut.parse('show ip interface brief ethernet0/1')
        var2 = uut.parse('show ip interface brief ethernet0/2')
        if var['interface']['Ethernet0/1']['ip_address'] != '192.168.2.2': self.failed('interface ethernet0/1 on router IOL 1 does not have a correct ip address')
        if var2['interface']['Ethernet0/2']['ip_address'] != '192.168.3.2': self.failed('interface ethernet0/2 on router IOL 1 does not have a correct ip address')

    @aetest.test
    def check_ip_correct_routeriol2(self, uut2):
        var = uut2.parse('show ip interface brief ethernet0/1')
        var2 = uut2.parse('show ip interface brief ethernet0/2')
        if var['interface']['Ethernet0/1']['ip_address'] != '192.168.2.3': self.failed('interface ethernet0/1 on router IOL 2 does not have a correct ip address')
        if var2['interface']['Ethernet0/2']['ip_address'] != '192.168.3.3': self.failed('interface ethernet0/2 on router IOL 2 does not have a correct ip address')

### cleanup actions ###
class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """

    # CommonCleanup follow exactly the same rule as CommonSetup regarding
    # subsection
    # You can have 1 to as many subsection as wanted

    @aetest.subsection
    def clean_device_config(self, uut, uut2):

        uut.configure("interface ethernet0/1\n" " no ip address\n" " sh\n")
        uut2.configure("interface ethernet0/1\n" " no ip address\n" " sh\n")

        uut.configure("interface ethernet0/2\n" " no ip address\n" " sh\n")
        uut2.configure("interface ethernet0/2\n" " no ip address\n" " sh\n")

    @aetest.subsection
    def disconnect(self, uut, uut2):
        """ Common Cleanup Subsection """
        uut.disconnect()
        uut2.disconnect()
