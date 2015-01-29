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

    def connect(self, host, port):
        # close old socket
        self.socket.close()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

        self.start()

    def send(self, message):
        if type(message) == bytes:
            bmsg = message

        else:
            bmsg = str(message).encode('utf8')

        self.socket.sendall(bmsg)

    def add_handler(self, handler):
        self.handlers.append(handler)

    def remove_handler(self, handler):
        self.handlers.remove(handler)

    def start(self):
        if hasattr(self, 'server'):
            self.server.running = False

        self.server = Server(self)

        self.server.start()

class Server(threading.Thread):
    """docstring for Server"""
    def __init__(self, connection):
        super(Server, self).__init__()
        self.connection = connection
        self.running = True
        self.conn = None
        self.addr = None

    def recv_message(self):
        """
        Receives a message from the socket.
        """
        byte = None
        msg = b''
        while byte != ETB:
            byte = self.connection.socket.recv(1)
            if byte != ETB:
                msg += byte
        return msg
        
    def run(self):
        """
        Code that should executed when thread is ran.
        """
        while self.running:
            if self.connection.connected:
                msg = self.recv_message()
                for handler in self.connection.handlers:
                    handler.handle_it(msg)

            else:
                self.connection.socket.listen(1)
                self.conn, self.addr = self.connection.socket.accept()
                self.connection.connected = True
