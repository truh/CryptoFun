#!/usr/bin/env python3

import socket
import sys


def serve(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        print(data.decode('utf8'), end='')
    conn.close()

if __name__ == '__main__':
    port = -1
    try:
        port = sys.argv
        port = port[1]
        port = int(port)
        assert port >= 1
        assert port <= 65535
    except Exception as e:
        print('Syntax: python Server.py <port>')
        print('err: ' + str(e))
        sys.exit(1)

    serve('0.0.0.0', port)
