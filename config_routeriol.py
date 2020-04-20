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

    @aetest.subsection
    def connect(self, testscript, testbed):
        """ Common Setup subsection """
        log.info("Aetest Common Setup ")

        testbed = load('routerIOL_tb.yaml')
        routeriol1 = testbed.devices['routeriol']
        routeriol2 = testbed.devices['routeriol2']
        routeriol3 = testbed.devices['routeriol3']

        routeriol1.connect()
        routeriol2.connect()
        routeriol3.connect()

        testscript.parameters['uut'] = routeriol1
        testscript.parameters['uut2'] = routeriol2
        testscript.parameters['uut3'] = routeriol3


### test cases ###
class test_cases(aetest.Testcase):
    """ Testcases section """

    @aetest.setup
    def configure_devices(self, section, uut, uut2, uut3):
        """ Testcase Setup section """
        log.info("Preparing the test")
        log.info(section)

        uut.configure("interface ethernet0/2\n" " ip address 192.168.5.1 255.255.255.0\n" " no sh\n")
        uut.configure("interface ethernet0/1\n" " ip address 192.168.2.1 255.255.255.0\n" " no sh\n")
        uut.configure("interface serial1/1\n" " ip address 10.0.2.1 255.255.255.254\n" " no sh\n")
        uut.configure("interface serial1/2\n" " ip address 10.0.3.1 255.255.255.254\n" " no sh\n")
        uut.configure("router eigrp 1\n" "eigrp router-id 1.1.1.1\n" " network 10.0.2.0\n" " network 10.0.3.0\n"
                      "network 192.168.5.0\n" "network 192.168.2.0\n" "passive-interface ethernet0/2\n "
                      "passive-interface ethernet0/0\n " "passive-interface ethernet0/1\n " " exit\n")

        uut2.configure("interface ethernet0/2\n" " ip address 192.168.6.1 255.255.255.0\n" " no sh\n")
        uut2.configure("interface ethernet0/1\n" " ip address 192.168.3.1 255.255.255.0\n" " no sh\n")
        uut2.configure("interface serial1/1\n" " ip address 10.0.2.2 255.255.255.254\n" " no sh\n")
        uut2.configure("interface serial1/0\n" " ip address 10.0.1.1 255.255.255.254\n" " no sh\n")
        uut2.configure("router eigrp 1\n" "eigrp router-id 2.2.2.2\n"" network 10.0.2.0\n" " network 10.0.1.0\n"
                       "network 192.168.6.0\n" "network 192.168.3.0\n" "passive-interface ethernet0/2\n "
                       "passive-interface ethernet0/0\n " "passive-interface ethernet0/1\n " " exit\n")

        uut3.configure("interface ethernet0/2\n" " ip address 192.168.7.1 255.255.255.0\n" " no sh\n")
        uut3.configure("interface ethernet0/1\n" " ip address 192.168.4.1 255.255.255.0\n" " no sh\n")
        uut3.configure("interface serial1/0\n" " ip address 10.0.1.2 255.255.255.254\n" " no sh\n")
        uut3.configure("interface serial1/2\n" " ip address 10.0.3.2 255.255.255.254\n" " no sh\n")
        uut3.configure("router eigrp 1\n" "eigrp router-id 3.3.3.3\n" " network 10.0.1.0\n" " network 10.0.3.0\n"
                       " network 192.168.7.0\n" "network 192.168.4.0\n" "passive-interface ethernet0/2\n "
                       "passive-interface ethernet0/0\n " "passive-interface ethernet0/1\n " " exit\n")

    @aetest.test
    def check_interfaces_routeriol1(self, uut):
        var = uut.parse('show ip interface brief')

        assert var['interface']['Ethernet0/1']['status'] == 'up', "interface ethernet0/1 on router IOL 1 is not up"
        assert var['interface']['Ethernet0/2']['status'] == 'up', "interface ethernet0/2 on router IOL 1 is not up"
        assert var['interface']['Serial1/1']['status'] == 'up', "interface Serial1/1 on router IOL 1 is not up"
        assert var['interface']['Serial1/2']['status'] == 'up', "interface Serial1/2 on router IOL 1 is not up"

        assert var['interface']['Ethernet0/1']['ip_address'] == '192.168.2.1', "interface ethernet0/1 on router IOL 1 " \
                                                                               "does not have a correct ip address "
        assert var['interface']['Ethernet0/2']['ip_address'] == '192.168.5.1', "interface ethernet0/2 on router IOL 1 " \
                                                                               "does not have a correct ip address "
        assert var['interface']['Serial1/1']['ip_address'] == '10.0.2.1', "interface serial1/1 on router IOL 1 does " \
                                                                          "not have a correct ip address "
        assert var['interface']['Serial1/2']['ip_address'] == '10.0.3.1', "interface serial1/2 on router IOL 1 does " \
                                                                          "not have a correct ip address "

    @aetest.test
    def check_interfaces_routeriol2(self, uut2):
        var = uut2.parse('show ip interface brief')
        assert var['interface']['Ethernet0/1']['status'] == 'up', "interface ethernet0/1 on router IOL 2 is not up"
        assert var['interface']['Ethernet0/2']['status'] == 'up', "interface ethernet0/2 on router IOL 2 is not up"
        assert var['interface']['Serial1/0']['status'] == 'up', "interface Serial1/0 on router IOL 2 is not up"
        assert var['interface']['Serial1/1']['status'] == 'up', "interface Serial1/1 on router IOL 2 is not up"

        assert var['interface']['Ethernet0/1']['ip_address'] == '192.168.3.1', "interface ethernet0/1 on router IOL 2 " \
                                                                               "does not have a correct ip address "
        assert var['interface']['Ethernet0/2']['ip_address'] == '192.168.6.1', "interface ethernet0/2 on router IOL 2 " \
                                                                               "does not have a correct ip address "
        assert var['interface']['Serial1/0']['ip_address'] == '10.0.1.1', "interface serial1/0 on router IOL 2 does " \
                                                                          "not have a correct ip address "
        assert var['interface']['Serial1/1']['ip_address'] == '10.0.2.2', "interface serial1/1 on router IOL 2 does " \
                                                                          "not have a correct ip address "

    @aetest.test
    def check_interfaces_routeriol3(self, uut3):
        var = uut3.parse('show ip interface brief')
        assert var['interface']['Ethernet0/1']['status'] == 'up', "interface ethernet0/1 on router IOL 3 is not up"
        assert var['interface']['Ethernet0/2']['status'] == 'up', "interface ethernet0/2 on router IOL 3 is not up"
        assert var['interface']['Serial1/2']['status'] == 'up', "interface Serial1/2 on router IOL 3 is not up"
        assert var['interface']['Serial1/0']['status'] == 'up', "interface Serial1/0 on router IOL 3 is not up"

        assert var['interface']['Ethernet0/1']['ip_address'] == '192.168.4.1', "interface ethernet0/1 on router IOL 3 " \
                                                                               "does not have a correct ip address "
        assert var['interface']['Ethernet0/2']['ip_address'] == '192.168.7.1', "interface ethernet0/2 on router IOL 3 " \
                                                                               "does not have a correct ip address "
        assert var['interface']['Serial1/0']['ip_address'] == '10.0.1.2', "interface serial1/0 on router IOL 3 does " \
                                                                          "not have a correct ip address "
        assert var['interface']['Serial1/2']['ip_address'] == '10.0.3.2', "interface serial1/2 on router IOL 3 does " \
                                                                          "not have a correct ip address "


### cleanup actions ###
class common_cleanup(aetest.CommonCleanup):
    """
    @aetest.subsection
    def clean_device_config(self, uut, uut2, uut3):
        uut.configure("interface ethernet0/1\n" " no ip address\n" " sh\n")
        uut.configure("interface ethernet0/2\n" " no ip address\n" " sh\n")
        uut.configure("interface serial1/1\n" " no ip address\n" " sh\n")
        uut.configure("interface serial1/2\n" " no ip address\n" " sh\n")

        uut2.configure("interface ethernet0/1\n" " no ip address\n" " sh\n")
        uut2.configure("interface ethernet0/2\n" " no ip address\n" " sh\n")
        uut2.configure("interface serial1/1\n" " no ip address\n" " sh\n")
        uut2.configure("interface serial1/0\n" " no ip address\n" " sh\n")

        uut3.configure("interface ethernet0/1\n" " no ip address\n" " sh\n")
        uut3.configure("interface ethernet0/2\n" " no ip address\n" " sh\n")
        uut3.configure("interface serial1/0\n" " no ip address\n" " sh\n")
        uut3.configure("interface serial1/2\n" " no ip address\n" " sh\n")

        uut.configure('no router eigrp 1');
        uut2.configure('no router eigrp 1');
        uut3.configure('no router eigrp 1');
    """
    @aetest.subsection
    def disconnect(self, uut, uut2, uut3):
        """ Common Cleanup Subsection """
        uut.disconnect()
        uut2.disconnect()
        uut3.disconnect()
