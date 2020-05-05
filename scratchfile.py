from IpExtractor import IpExtractorClass

ip1 = IpExtractorClass()
res = ip1.extractip('10.100.244.1', '45569', 'ethernet0/0')
print (res)