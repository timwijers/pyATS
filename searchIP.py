import requests
import re
import yaml


url = "http://10.100.244.1/dhcpd.html"
request = requests.get(url)
content = request.text

IPDict = {"DockerHost": "", "FortiGate": "", "Router1": "", "Router2": "", "Router3": "", "Router5": ""}

def getIP(line):
    ipsFound = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', line)
    return ipsFound


for line in content.split("<tr>"):
    if 'ubuntu1804-pfne' in line:
        IPDict["DockerHost"] = getIP(line)
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

for line in listoftestbedfile:
    print(listoftestbedfile)
'''
    if 'routeriol' in line:
        line["connections"]["cli"]["ip"] = IPDict["Router1"]
        
    if line[0]["alias"] == "uut2":
        line["connections"]["cli"]["ip"] = IPDict["Router2"]
    if line[0]["alias"] == "uut3":
        line["connections"]["cli"]["ip"] = IPDict["Router3"]
    if line[0]["alias"] == "uut5":
        line["connections"]["cli"]["ip"] = IPDict["Router5"]
   '''
with open("routerIOL_tb.yaml", "w") as testbedfile:
    yaml.dump(listoftestbedfile, testbedfile, default_flow_style=False, sort_keys=False)

