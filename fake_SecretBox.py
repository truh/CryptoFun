class FakeSecretBox(object):
    def __init__(self):
        super(FakeSecretBox, self).__init__()

    def encrypt(self, plain):
        return plain

    def decrypt(self, cipher):
        return cipher
