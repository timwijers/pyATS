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

        dev = testbed.devices['routeriol']
        dev.connect(alias= 'uut', via='cli')

        dev2 = testbed.devices['routeriol2']
        dev2.connect(alias='uut2', via='cli')

        testscript.parameters['uut'] = dev
        testscript.parameters['uut2'] = dev2


### test cases ###
class test_cases(aetest.Testcase):
    """ This is user Testcases section """

    @aetest.setup
    def setup_testCases(self, section):
        """ Testcase Setup section """
        log.info("Preparing the test")
        log.info(section)

    @aetest.test
    def send_show_int_cmd(self, uut):

        self.output = uut.execute('show ip interface brief')

    @aetest.test
    def conf_int_e01_cmd(self, uut):

        check_pre = uut.execute('show ip int brief ethernet0/1')
        uut.configure("interface ethernet0/1\n" " ip address 192.168.1.6 255.255.255.0\n" " no sh\n")
        time.sleep(15)
        check_post = uut.execute('show ip int brief ethernet0/1')
        if check_post == check_pre: self.failed("wrong ip address")


### cleanup actions ###
class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """


    @aetest.subsection
    def disconnect(self, uut):
        """ Common Cleanup Subsection """
        uut.disconnect()
