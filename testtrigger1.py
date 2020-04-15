# Python imports
import time
import logging

# pyATS import
from pyats import aetest
from genie.harness.base import Trigger

log = logging.getLogger()

class connectionTrigger(Trigger):

   @aetest.setup
    def prerequisites(self, uut):
        '''Check current IP'''

        # Parse output
        output = uut.parse('show interface brief ethernet0/1')
        self.ip = output['ip_address']

   @aetest.test
    def setIP(self, uut):
        '''Set IP'''
        uut.configure("interface ethernet0/1\n" " ip address 192.168.1.2 255.255.255.0")

   @aetest.test
    def verifyIP(self, uut):
        '''Verify if the IP address is correctly set'''

        output = uut.parse('show ip interface brief ethernet0/1')


        if output[ip_address] != "192.168.1.2":
            self.failed("IP is not correctly set")

