#!/usr/bin/python

import sys
from sys import argv
import socket

if len(argv) != 3:
    print "Usage: ./server.py [host] [port]"
    exit(1)

script, host, port = argv
