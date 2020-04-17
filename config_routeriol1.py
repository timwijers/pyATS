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
    def setup_testCases(self, section):
        """ Testcase Setup section """
        log.info("Preparing the test")
        log.info(section)

    @aetest.test
    def check_if_not_down_routeriol1(self, uut):
        var = uut.parse('show ip interface brief ethernet0/2')
        print(var)
        if var['status'] != 'up': self.failed('interface ethernet0/2 is not up')

    @aetest.test
    def check_if_not_down_routeriol2(self, uut2):
        var = uut2.parse('show ip interface brief ethernet0/2')
        if var['status'] != 'up': self.failed('interface ethernet0/2 is not up')



### cleanup actions ###
class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """

    # CommonCleanup follow exactly the same rule as CommonSetup regarding
    # subsection
    # You can have 1 to as many subsection as wanted

    @aetest.subsection
    def disconnect(self, uut, uut2):
        """ Common Cleanup Subsection """
        uut.disconnect()
        uut2.disconnect()
