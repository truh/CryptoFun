"""

"""


from cryptofun import Connection


class Application(object):
    """docstring for Application"""
    def __init__(self):
        super(Application, self).__init__()

    def main(self, argv):
        print(argv[0])
        print(argv[1])
        conn = Connection(port=int(argv[1]))
