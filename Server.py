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
    # generate server keypair
    server_keypair = libnacl.public.SecretKey()

    # receive clients public key
    client_pk = conn.recv(1024)
    print("Received public key from client: {client_pk}"
        .format(client_pk=base64.b16encode(client_pk)))

    # send public key to client
    conn.sendall(server_keypair.pk)
    print("Send public key to client: {server_pk}"
        .format(server_pk=base64.b16encode(server_keypair.pk)))

    # create encryption box
    box = libnacl.public.Box(server_keypair.sk, client_pk)
    
    # generate symmetric encryption key
    symmetric_box = libnacl.secret.SecretBox()
    print("Sent symmetric key to client: {symmetric_key}"
        .format(symmetric_key=base64.b16encode(symmetric_box.sk)))

    # encrypt symmetric encryption key
    encrypted_symmetric_key = box.encrypt(symmetric_box.sk)

    # transmit encrypted symmetric key
    conn.sendall(encrypted_symmetric_key)

    # return symmetric box
    return symmetric_box

def serve(host, port, encrypted=False):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()

    print('Connected by', addr)

    symmetric_box = FakeSecretBox()
    if encrypted:
        symmetric_box = key_exchange(conn)
        print('Established encrypted connection.')

    while True:
        data = conn.recv(1024)
        if not data: break
        data = symmetric_box.decrypt(data)
        data = data.decode('utf8')
        print(data, end='')
    conn.close()

if __name__ == '__main__':
    port = -1
    encrypted = False

    try:
        port = sys.argv
        port = port[1]
        port = int(port)
        assert port >= 1
        assert port <= 65535

    except Exception as e:
        print('Syntax: python Server.py <port> [encrypted]')
        print('err: ' + str(e))
        sys.exit(1)

    if len(sys.argv) > 2:
        encrypted = sys.argv[2] == 'encrypted'

    serve('0.0.0.0', port, encrypted=encrypted)
