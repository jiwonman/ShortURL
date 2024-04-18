import random

KEY_LEN = 6

class Base62():
    encoding = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" * KEY_LEN

    def encode(self):
        key = "".join(random.sample(self.encoding, KEY_LEN))
        return key


