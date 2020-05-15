__Author__ = 'Tim Wijers'
__Copyright__ = 'Routz B.V'
__Date__ = 'May 2020'

import requests
import re
import yaml
import time
import telnetlib

eveIP = '10.100.244.1'
url = "http://" + eveIP + "/dhcpd.html"
content = requests.get(url).text
dockerHost_pfne_uname_pwd = ' ansible_ssh_pass=pfne ansible_ssh_user=pfne ansible_sudo_pass=root'
ansibleHostsFileContent = ['[dockerHost]', '', '\n', '[dockerHost:vars]', 'ansible_python_interpreter=/usr/bin'
                                                                          '/python3', '\n', '[localhost]', '127.0.0.1',
                           '[localhost:vars]',
                           'ansible_python_interpreter=/usr/bin/python3']

IPDict = {"FortiGate": "", "Router1": "", "Router2": "", "Router3": "", "Router5": ""}

tbfilecontent = {
    'devices': {
        'routeriol': {
            'type': 'router',
            'os': 'ios',
            'alias': 'uut',
            'credentials': {
                'default': {
                    'username': 'cisco',
                    'password': 'cisco'}},
            'connections': {
                'cli': {
                    'protocol': 'ssh',
                    'ip': '',
                    'username': 'cisco',
                    'password': 'cisco'}}},
        'routeriol2': {
            'type': 'router',
            'os': 'ios',
            'alias': 'uut2',
            'credentials': {
                'default': {
                    'username': 'cisco',
                    'password': 'cisco'}},
            'connections': {
                'cli': {
                    'protocol': 'ssh',
                    'ip': '',
                    'username': 'cisco',
                    'password': 'cisco'}}},
        'routeriol3': {
            'type': 'router',
            'os': 'ios',
            'alias': 'uut3',
            'credentials': {
                'default': {
                    'username': 'cisco',
                    'password': 'cisco'}},
            'connections': {
                'cli': {
                    'protocol': 'ssh',
                    'ip': '',
                    'username': 'cisco',
                    'password': 'cisco'}}},
        'routeriol5': {
            'type': 'router',
            'os': 'ios',
            'alias': 'uut5',
            'credentials': {
                'default': {
                    'username': 'cisco',
                    'password': 'cisco'}},
            'connections': {
                'cli': {
                    'protocol': 'ssh',
                    'ip': '',
                    'username': 'cisco',
                    'password': 'cisco'
                }}}}}


def getIP(line):
    ipsFound = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', line)
    return str(ipsFound).strip('[]').strip("''")


def setSSH_IOL(ip, port, hostname):
    telNetSession = telnetlib.Telnet()

    telNetSession.open(ip, port)

    time.sleep(5)
    telNetSession.write(' enable\n'.encode('ascii'))
    time.sleep(2)
    telNetSession.write('conf terminal\n'.encode('ascii'))
    time.sleep(2)
    telNetSession.write('hostname ' + hostname + '\n'.encode('ascii'))
    time.sleep(2)
    telNetSession.write('crypto key generate rsa\n'.encode('ascii'))
    time.sleep(2)
    telNetSession.write('1024\n'.encode('ascii'))
    time.sleep(5)
    telNetSession.write('line vty 0 4\n'.encode('ascii'))
    time.sleep(2)
    telNetSession.write('transport input ssh\n'.encode('ascii'))
    time.sleep(2)
    telNetSession.write('login local\n'.encode('ascii'))
    time.sleep(2)
    telNetSession.write('password cisco\n'.encode('ascii'))
    time.sleep(2)
    telNetSession.write('end\n'.encode('ascii'))
    time.sleep(2)
    telNetSession.write('conf terminal\n'.encode('ascii'))
    time.sleep(2)
    telNetSession.write('username cisco password cisco\n'.encode('ascii'))

    print(telNetSession.read_very_eager())


for line in content.split("<tr>"):
    if 'ubuntu1804-pfne' in line:
        ansibleHostsFileContent[1] = getIP(line) + dockerHost_pfne_uname_pwd
    if 'FortiGate-VM64-KVM' in line:
        IPDict["FortiGate"] = getIP(line)
    if 'aa:bb:cc:00:14' in line:
        IPDict["Router1"] = getIP(line)
    if 'aa:bb:cc:00:24' in line:
        IPDict["Router2"] = getIP(line)
    if 'aa:bb:cc:00:34' in line:
        IPDict["Router3"] = getIP(line)
    if 'aa:bb:cc:00:64' in line:
        IPDict["Router5"] = getIP(line)

print(IPDict)
print(ansibleHostsFileContent)
for key, value in tbfilecontent['devices'].items():
    if value['alias'] == 'uut':
        value['connections']['cli']['ip'] = (IPDict.get("Router1"))
    if value['alias'] == 'uut2':
        value['connections']['cli']['ip'] = (IPDict.get("Router2"))
    if value['alias'] == 'uut3':
        value['connections']['cli']['ip'] = (IPDict.get("Router3"))
    if value['alias'] == 'uut5':
        value['connections']['cli']['ip'] = (IPDict.get("Router5"))

print(tbfilecontent)

with open("routerIOL_tb.yaml", "a") as testbedfile:
    testbedfile.truncate(0)
    yaml.dump(tbfilecontent, testbedfile, default_flow_style=False, sort_keys=False)

ansibleHostsFile = open("hosts", "a")
ansibleHostsFile.truncate(0)
ansibleHostsFile.writelines("%s\n" % line for line in ansibleHostsFileContent)
ansibleHostsFile.close()

setSSH_IOL('10.100.244.1', '45569', 'Router1')
setSSH_IOL('10.100.244.1', '45570', 'Router2')
setSSH_IOL('10.100.244.1', '45571', 'Router3')
setSSH_IOL('10.100.244.1', '45574', 'Router5')
