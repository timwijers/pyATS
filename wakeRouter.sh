#!/usr/bin/expect

spawn telnet 10.100.244.1 45569
expect "'^]'."
send "\n"
send "\x1b\r"

expect "telnet>"
send "close\r"


spawn telnet 10.100.244.1 45570
expect "'^]'."
send "\n"
send "\x1b\r"

expect "telnet>"
send "close\r"

spawn telnet 10.100.244.1 45571
expect "'^]'."
send "\n"
send "\x1b\r"

expect "telnet>"
send "close\r"

spawn telnet 10.100.244.1 45574
expect "'^]'."
send "\n"
send "\x1b\r"

expect "telnet>"
send "close\r"