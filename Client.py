#!/usr/bin/env python3

import socket
import sys


def loop(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:
        line = sys.stdin.readline()
        line = line.encode('utf8')
        s.sendall(line)
    conn.close()

if __name__ == '__main__':
    host = None
    port = -1

    try:
        host = sys.argv
        host = host[1]
        assert host != None
        assert host is not ''

        port = sys.argv
        port = port[2]
        port = int(port)
        assert port >= 1
        assert port <= 65535

    except Exception as e:
        print('Syntax: python Client.py <host> <port>')
        print('err: ' + str(e))
        sys.exit(1)

    loop(host, port)
