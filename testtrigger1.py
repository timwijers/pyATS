# Python imports
import time
import logging

# pyATS import
from pyats import aetest
from genie.harness.base import Trigger

log = logging.getLogger()
"""
class connectionTrigger(Trigger):

   @aetest.setup
   def connect(self):
        '''Check current IP'''

        # Parse output
        log.info(parse('show interface brief ethernet0/1'))
        self.ip = output['ip_address']

   @aetest.test
   def setIP(self):
        '''Set IP'''
        uut.configure("interface ethernet0/1\n" " ip address 192.168.1.2 255.255.255.0")

   @aetest.test
   def verifyIP(self):
        '''Verify if the IP address is correctly set'''

        output = uut.parse('show ip interface brief ethernet0/1')


        if output[ip_address] != "192.168.1.2":
            self.failed("IP is not correctly set")
"""

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


class test_up_interface(aetest.Testcase):
    """ This is user Testcases section """

    # Testcases are divided into 3 sections
    # Setup, Test and Cleanup.

    # This is how to create a setup section
    @aetest.setup
    def send_command(self, uut):
        # Get device output
        self.output = uut.execute('show interface')

class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """

    # CommonCleanup follow exactly the same rule as CommonSetup regarding
    # subsection
    # You can have 1 to as many subsection as wanted

    @aetest.subsection
    def disconnect(self, uut):
        """ Common Cleanup Subsection """
        uut.disconnect()
