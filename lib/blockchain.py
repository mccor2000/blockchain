import hashlib
import json
from urllib.parse import urlparse

from .block import Block
from .transaction import Transaction

class Blockchain:

    def __init__(self):

        self.current_transactions = []
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

        block = Block(
            index=len(self.chain) + 1,
            transactions=self.current_transactions,
            proof=proof,
            previous_hash=previous_hash
        )

        self.current_transactions = []
        self.chain.append(block)

        return block


    def new_transaction(self, sender, recipient, amount):

        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)

        return self.last_block['index'] + 1


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

            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False

            last_block = block
            current_index += 1

        return True

    def proof_of_work(self, last_block):

        last_proof = last_block['proof']
        last_hash = last_block.hash()

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof, last_hash):

        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
