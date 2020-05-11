from Scratchfiles.IpExtractor import extractip
import yaml

ip1 = extractip('10.100.244.1', '45569', 'ethernet0/0')
ip2 = extractip('10.100.244.1', '45570', 'ethernet0/0')
ip3 = extractip('10.100.244.1', '45571', 'ethernet0/0')
print('pyATS_Router 1 IP-Adres: ' + ip1)
print('pyATS_Router 2 IP-Adres: ' + ip2)
print('pyATS_Router 3 IP-Adres: ' + ip3)

with open('../routerIOL_tb.yaml') as file:
    loadedData = yaml.load(file, Loader=yaml.)
    print(loadedData)
