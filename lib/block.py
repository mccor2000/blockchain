class Block:

    def __init__(self, index, transactions = [], proof = 100, previous_hash = '1'):
        self.index = index
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash
