import telnetlib

TelNetSession = telnetlib.Telnet('10.100.244.1', 45569)



TelNetSession.write("enable\n")
TelNetSession.write("show ip int brief ethernet0/0\n")


print(TelNetSession.read_all())