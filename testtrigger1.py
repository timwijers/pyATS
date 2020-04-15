# Python imports
import time
import logging

# pyATS import
from pyats import aetest
from genie.harness.base import Trigger

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
        for device in testbed:
            # Connecting to the devices using the default connection
            device.connect(via ='cli')

        # Save it in testscript parmaeters to be able to use it from other
        # test sections
        testscript.parameters['uut'] = device

### test cases ###
class test_cases (aetest.Testcase):
    """ This is user Testcases section """

    # Testcases are divided into 3 sections
    # Setup, Test and Cleanup.

    # This is how to create a setup section
    @aetest.setup
    def setup_testCases(self, section):
        """ Testcase Setup section """
        log.info("Preparing the test")
        log.info(section)

    @aetest.test
    def send_show_int_cmd(self, uut):
        # Get device output
        self.output = uut.execute('show ip interface brief')

    @aetest.test
    def conf_int_e01_cmd(self, uut):
        # Get device output
        uut.execute('configure terminal')
        uut.execute('interface ethernet0/1')
        uut.execute('ip address 192.168.1.5 255.2355.255.0')
        uut.execute('no sh')
        uut.execute('exit')
        check = uut.parse('show ip int brief ethernet0/1')
        if check[ip_address] != '192.168.1.5': self.failed("wrong ip address")


### cleanup actions ###
class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """

    # CommonCleanup follow exactly the same rule as CommonSetup regarding
    # subsection
    # You can have 1 to as many subsection as wanted

    @aetest.subsection
    def disconnect(self, uut):
        """ Common Cleanup Subsection """
        uut.disconnect()
