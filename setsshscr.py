import time
import telnetlib

ip = '10.100.244.1'
portList = [45569, 45570, 45571, 45574]
hostnameList = ['Router1', 'Router2', 'Router3', 'Router5']
count = 0

telNetSession = telnetlib.Telnet()
for port in portList:
    telNetSession.open(ip, port)

    time.sleep(5)
    telNetSession.write(' enable\n')
    time.sleep(2)
    telNetSession.write('conf terminal\n')
    time.sleep(2)
    telNetSession.write('hostname ' + hostnameList[count] + '\n')
    time.sleep(2)
    telNetSession.write('crypto key generate rsa\n')
    time.sleep(2)
    telNetSession.write('1024\n')
    time.sleep(5)
    telNetSession.write('line vty 0 4\n')
    time.sleep(2)
    telNetSession.write('transport input ssh\n')
    time.sleep(2)
    telNetSession.write('login local\n')
    time.sleep(2)
    telNetSession.write('password cisco\n')
    time.sleep(2)
    telNetSession.write('end\n')
    time.sleep(2)
    telNetSession.write('conf terminal\n')
    time.sleep(2)
    telNetSession.write('username cisco password cisco\n')
    count += 1
    print(telNetSession.read_very_eager())
