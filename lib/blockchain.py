import hashlib
from urllib.parse import urlparse

from .block import Block
from .transaction import Transaction


class Blockchain:
    def __init__(self):

        self.current_transactions = []
        self.validated_transactions = []

        self.chain = []
        self.nodes = set()

        self.new_block(proof=100, previous_hash='1')

    @property
    def last_block(self):
        return self.chain[-1]

    @property
    def size(self):
        return len(self.chain)

    def new_block(self, proof, previous_hash):

        block = Block(index=self.size + 1,
                      transactions=self.validated_tx,
                      proof=proof,
                      previous_hash=previous_hash)

        self.validated_tx = []
        self.chain.append(block)

        return block

    def register_node(self, address):

        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')

    def valid_chain(self, chain):

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]

            last_block_hash = last_block.hash()
            if block['previous_hash'] != last_block_hash:
                return False

            if not self.valid_proof(last_block['proof'], block['proof'],
                                    last_block_hash):
                return False

            last_block = block
            current_index += 1

        return True

    @staticmethod
    def valid_proof(last_proof, proof, last_hash):

        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
