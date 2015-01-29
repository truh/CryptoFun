"""

"""


import sys

from cryptofun.connection import Connection


def command_connect(line, app):
    print('cryptofun::application::command_connect(line={line}, app={app}'.format(line=line, app=app))
    params = line.split(' ')[1:]
    if len(params) != 2:
        print("SYNTAX: !connect <host> <port>")
        globals = debugger.run(setup['file'], None, None)

    else:
        host = str(params[0])
        port = int(params[1])
        app.conn.connect(host, port)


class Application(object):
    """docstring for Application"""
    def __init__(self):
        super(Application, self).__init__()

        self.command_handlers = {
            '!connect': command_connect,
        }

    def main(self, argv):
        if len(argv) < 2:
            print('Please pass a port number as argument.')

        self.conn = Connection(port=int(argv[1]))
        self.conn.start()

        while True:
            self.io()

    def io(self):
        line = sys.stdin.readline()

        maybe_cmd = ""

        try:
            maybe_cmd = line.split(' ')[0]
        except:
            pass

        if maybe_cmd in self.command_handlers:
            self.command_handlers[maybe_cmd](line, self)
        else:
            try:
                self.conn.send(line)
            except:
                pass
