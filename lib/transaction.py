import json
from base64 import b64decode, b64encode

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Transaction:
    def __init__(self, sender, recipient, amount, signature=None):

        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def hash(self):

        tx_content = json.dumps({
            'sender': self.sender.hex(),
            'recipient': self.recipient,
            'amount': self.amount
        })
        return SHA256.new(str.encode(tx_content))

    def sign(self, private_key):

        signature = PKCS1_v1_5.new(private_key).sign(msg_hash=self.hash())
        if not signature:
            print('Signing transaction failed')
            return False

        self.signature = signature
        return True

    @staticmethod
    def validate(tx):

        public_key = RSA.importKey(b64decode(tx.sender))
        validator = PKCS1_v1_5.new(public_key)

        is_valid = validator.verify(tx.hash(), tx.signature)
        if not is_valid:
            print('Verifying failed')
            return False

        return True
