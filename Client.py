#!/usr/bin/env python3

import base64
import libnacl
import libnacl.public
import libnacl.secret
import libnacl.utils
import socket
import sys

from fake_SecretBox import FakeSecretBox


def key_exchange(conn):
    # generate clients keypair
    client_keypair = libnacl.public.SecretKey()

    # send public key to server
    conn.sendall(client_keypair.pk)
    print("Send public key to server: {client_pk}"
        .format(client_pk=base64.b16encode(client_keypair.pk)))

    # receive servers public key
    server_pk = conn.recv(1024)
    print("Received public key from client: {server_pk}"
        .format(server_pk=base64.b16encode(server_pk)))

    # create encryption box
    box = libnacl.public.Box(client_keypair.sk, server_pk)

    # receive encrypted symmetric key
    encrypted_symmetric_key = conn.recv(1024)

    # decrypt symmetric key
    symmetric_key = box.decrypt(encrypted_symmetric_key)
    symmetric_box = libnacl.secret.SecretBox(symmetric_key)
    print("Received symmetric key from the server: {symmetric_key}"
        .format(symmetric_key=base64.b16encode(symmetric_box.sk)))

    # return symmetric key
    return symmetric_box

def loop(host, port, encrypted=False):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    symmetric_box = FakeSecretBox()
    if encrypted:
        symmetric_box = key_exchange(s)

    while True:
        line = sys.stdin.readline()
        line = line.encode('utf8')
        line = symmetric_box.encrypt(line)
        s.sendall(line)
    conn.close()

if __name__ == '__main__':
    host = None
    port = -1
    encrypted = False

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
        print('Syntax: python Client.py <host> <port> [encrypted]')
        print('err: ' + str(e))
        sys.exit(1)

    if len(sys.argv) > 3:
        encrypted = sys.argv[3] == 'encrypted'

    loop(host, port, encrypted=encrypted)
