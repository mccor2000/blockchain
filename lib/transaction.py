from Crypto.Hash import SHA256
from base64 import (
    b64encode, 
    b64decode
)

class Transaction:

    def __init__(self, sender, recipient, amount):

        self.sender = sender
        self.recipient= recipient
        self.amount = amount
        self.signature = None

    def hash(self):
        pass

    def sign(self):
        pass

    @staticmethod
    def validate(tx):
        pass

    @staticmethod
    def import_from_file(path):
        pass

    @staticmethod
    def export_to_file(tx):
        pass
