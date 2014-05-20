#!/usr/bin/python

import sys, socket, signal, os
from sys import argv

def handler(signum, frame):
    clntFile.close()
    clntSock.close()
    exit(0)

signal.signal(signal.SIGINT, handler)

if len(argv) != 3:
    print "Usage: ./server.py [port] [root]"
    exit(1)

host = ''
port = int(argv[1])
root = argv[2]

servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

servSock.bind((host, port))

servSock.listen(1)

while True:
    clntSock, clntAddr = servSock.accept()
    clntIP = clntSock.getpeername()[0]
    clntFile = clntSock.makefile("rw", 0)

    reqLine = clntFile.readline().strip()

    method, page, protocol = reqLine.split()

    filename = root + page
    if filename[-1] == '/':
        filename = filename + "index.html"
    if os.path.isfile(filename):
        readFile = open(filename)

        clntFile.write("HTTP/1.0 200 OK\r\n\r\n")
        for line in readFile:
            clntFile.write(line)

        print "%s: %s" % (clntIP, reqLine)
        readFile.close()
    else:
        clntFile.write("HTTP/1.0 404 NOT FOUND\r\n\r\n<html><body><h1>404 Not Found</h1><body><html>")

    clntFile.close()
