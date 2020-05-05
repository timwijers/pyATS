import telnetlib
import re
import time


class IpExtractorClass:

    def extractip(self, ip, port, interface):
        regexPatt = re.compile('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}'
                               + '(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')
        telNetSession = telnetlib.Telnet()

        telNetSession.open(ip, port)

        time.sleep(2)

        telNetSession.write('enable\n')
        telNetSession.write('show ip int brief' + interface + '\n')

        time.sleep(2)

        ResultString = telNetSession.read_very_eager()

        ExtractedIpAddress = regexPatt.search(ResultString)
        telNetSession.close()

        return ResultString
