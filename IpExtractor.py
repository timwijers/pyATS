import telnetlib
import re
import time



ipRegexPatt = re.compile('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}'
                                 + '(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')

telNetSession = telnetlib.Telnet()

telNetSession.open('10.100.244.1', '45569')

time.sleep(2)

telNetSession.write('enable\n')
telNetSession.write('show ip int brief ethernet0/0\n')

time.sleep(2)

ResultString = telNetSession.read_very_eager()
telNetSession.close()

ExtractedIpAddress = ipRegexPatt.search(ResultString)

print(ResultString)
print(ExtractedIpAddress)
