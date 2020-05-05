import telnetlib
import re
'''
IpRegexPatt= re.compile('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}'
                +'(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')

TelNetSession = telnetlib.Telnet()

TelNetSession.open('10.100.244.1', '45569')

TelNetSession.write('enable\n')
TelNetSession.write('show ip int brief ethernet0/0\n')

ResultString = TelNetSession.read_very_eager()
#TelNetSession.close()

ExtractedIpAddress = IpRegexPatt.search(ResultString)
print(ResultString)
print(ExtractedIpAddress)
'''
import telnetlib
tn= telnetlib.Telnet()
tn.open('10.100.244.1', '45569')
tn.write('enable\n')
tn.write('show ip int brief ethernet0/0\n')
res = tn.read_very_eager()
print(res)
