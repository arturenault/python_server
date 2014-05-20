#!/usr/bin/python

import sys
from sys import argv
import socket

if len(argv) != 3:
    print "Usage: ./server.py [port] [root]"
    exit(1)

host = ""
script, port, root = argv

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(host, port)

sock.listen(1)
