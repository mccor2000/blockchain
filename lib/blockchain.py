# from base64 import b64encode
from urllib.parse import urlparse

from block import Block
# from Crypto.PublicKey import RSA
from transaction import Transaction


class Blockchain:
    def __init__(self):

        self.current_transaction = None
        self.chain = []
        self.nodes = set()

        self.__new_block(previous_hash='0')

    @property
    def last_block(self):
        return self.chain[-1]

    @property
    def size(self):
        return len(self.chain)

    def generate_block(self):
        previous_hash = self.last_block.hash()

        return self.__new_block(previous_hash)

    def __new_block(self, previous_hash):

        block = Block(index=self.size + 1,
                      transaction=self.current_transaction,
                      previous_hash=previous_hash)

        self.validated_tx = []
        self.chain.append(block)

        return block

    def new_transaction(self, tx_content):

        transaction = Transaction(**tx_content)
        self.current_transaction = transaction

        return transaction

    def register_node(self, address):

        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')


# testing

# ledger = Blockchain()
# print(ledger.size)
# print(ledger.last_block.__dict__)

# Create transaction
# private_key = ''
# with open('../keys/private_key.pem', 'r') as f:
#     private_key = RSA.importKey(f.read())
#
# tx = Transaction(b64encode(private_key.public_key().exportKey('PEM')),
#                  'grimmz', 6)
# tx.sign(private_key)
#
# ledger.new_transaction(tx.__dict__)
# ledger.generate_block()
#
# print(ledger.size)
# print(ledger.last_block.__dict__)
