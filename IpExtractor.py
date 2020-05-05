import telnetlib
import re
import time


class IpExtractorClass:

    def extractip(self, ip, port, interface):
        regexPatt = re.compile('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}'
                               + '(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')
        telNetSession = telnetlib.Telnet()

        # telNetSession.open(ip, port)
        telNetSession.open('10.100.244.1', '45569')
        time.sleep(5)

        telNetSession.write('enable\n')
        telNetSession.write('show ip int brief ethernet 0/0\n')
        # telNetSession.write('show ip int brief' + interface + '\n')
        time.sleep(5)

        ResultString = telNetSession.read_very_eager()
        print('Resultaat' + ResultString)
        ExtractedIpAddress = regexPatt.search(ResultString)
        #telNetSession.close()

        return ResultString
