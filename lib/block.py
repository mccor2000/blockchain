import json

from Crypto.Hash import SHA256


class Block:
    def __init__(self, index, transactions=[], proof=100, previous_hash='1'):

        self.index = index
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash

    def hash(self):

        block_content = json.dumps(self.__dict__)
        return SHA256.new(str.encode(block_content))
