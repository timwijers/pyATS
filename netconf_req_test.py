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
            device.connect(via='netconf')

        # Save it in testscript parmaeters to be able to use it from other
        # test sections
        testscript.parameters['uut'] = device


### test cases ###
class test_cases(aetest.Testcase):



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
