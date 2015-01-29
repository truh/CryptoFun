"""

"""

import socket
import threading

# Start of Heading
SOH = 0x01

# End Transmission Block character
ETB = 0xC0

class Connection(object):
    """docstring for Connection"""
    def __init__(self, host:str='0.0.0.0', port:int=57575):
        super(Connection, self).__init__()

        self.connected = False

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))

        self.handlers = []

    def connect(host, port):
        # close old socket
        self.socket.close()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def send(message):
        if type(message) == bytes:
            bmsg = message

        else:
            bmsg = str(message).encode('utf8')

        self.socket.sendall(bmsg)

    def add_handler(handler):
        self.handlers.append(handler)

    def remove_handler(handler):
        self.handlers.remove(handler)


class Server(object):
    """docstring for Server"""
    def __init__(self, connection):
        super(Server, self).__init__()
        self.connection = connection
        self.running = True
        self.conn = None
        self.addr = None

    def recv_message():
        """
        Receives a message from the socket.
        """
        byte = None
        msg = b''
        while byte != ETB:
            byte = self.socket.recv(1)
            if byte != ETB:
                msg += byte
        return msg
        
    def run():
        """
        Code that should executed when thread is ran.
        """
        while self.running:
            if self.connection.connected:
                msg = recv_message()
                for handler in self.connection.handlers:
                    handler.handle_it(msg)

            else:
                s.listen(1)
                self.conn, self.addr = s.accept()
                self.connection.connected = True
