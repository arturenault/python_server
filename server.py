#!/usr/bin/python

import sys
from sys import argv
import socket

if len(argv) != 2:
    print "Usage: ./server.py [port]"
    exit(1)

host = ''
port = int(argv[1])

servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

servSock.bind((host, port))

servSock.listen(1)

while True:
    clntSock, clntAddr = servSock.accept()
    clntIP = clntSock.getpeername()[0]
    clntFile = clntSock.makefile("rw", 0)

    line = clntFile.readline().strip()

    clntFile.write('HTTP/1.0 200 OK\n\n')
    clntFile.write('<html><head><title>Welcome %s!</title></head>' % str(clntAddr))
    clntFile.write('<body><h1>Follow the link...</h1>')
    clntFile.write('All the server needs to do is ')
    clntFile.write('to deliver the text to the socket. ')
    clntFile.write('It delivers the HTML code for a link, ')
    clntFile.write('and the web browser converts it. <br><br><br><br>')
    clntFile.write('<font size="7"><center> <a href="http://python.about.com/index.html">Click me!</a> </center></font>')
    clntFile.write('<br><br>The wording of your request was: "%s"' % line )
    clntFile.write('</body></html>')

    print "%s: %s" % (clntIP, line)
    clntFile.close()
