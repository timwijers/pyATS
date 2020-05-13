__Author__ = 'Tim Wijers'
__Copyright__ = 'Routz B.V'
__Date__ = 'May 2020'

import requests
import re
import yaml

url = "http://10.100.244.1/dhcpd.html"
content = requests.get(url).text
ansibleHostsFileContent = ['[dockerHost]', '', '\n', '[dockerHost:vars]', 'ansible_python_interpreter=/usr/bin'
                                                                          '/python3']
IPDict = {"DockerHost": "", "FortiGate": "", "Router1": "", "Router2": "", "Router3": "", "Router5": ""}


def getIP(line):
    ipsFound = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', line)
    return str(ipsFound).strip('[]').strip("''")


for line in content.split("<tr>"):
    if 'ubuntu1804-pfne' in line:
        ansibleHostsFileContent[1] = getIP(line)
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

with open("routerIOL_tb.yaml") as testbedfile:
    listoftestbedfile = yaml.load(testbedfile,Loader=yaml.Loader)

print(listoftestbedfile)

for key, value in listoftestbedfile['devices'].items():
        if value['alias'] == 'uut':
            value['connections']['cli']['ip'] = (IPDict.get("Router1"))
        if value['alias'] == 'uut2':
            value['connections']['cli']['ip'] = (IPDict.get("Router2"))
        if value['alias'] == 'uut3':
            value['connections']['cli']['ip'] = (IPDict.get("Router3"))
        if value['alias'] == 'uut5':
            value['connections']['cli']['ip'] = (IPDict.get("Router5"))

print(listoftestbedfile)

with open("routerIOL_tb.yaml", "w") as testbedfile:
    yaml.dump(listoftestbedfile, testbedfile, default_flow_style=False, sort_keys=False)

ansibleHostsFile = open("hosts", "a")
ansibleHostsFile.truncate(0)
ansibleHostsFile.writelines("%s\n" % line for line in ansibleHostsFileContent)
ansibleHostsFile.close()