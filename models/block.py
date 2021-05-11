import hashlib

class Block:

    def __init__(self, data, previousHash, timestamp):
        self.data = data
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.nonce = 0
        self.hash = self.calculateHash()
        
    def calculateHash(self):
        return hashlib.sha256(str(self.nonce).encode('utf-8') + str(self.data).encode('utf-8') + self.previousHash.encode('utf-8') + str(self.timestamp).encode('utf-8')).hexdigest()

    def mineBlock(self, difficulty):
        checkStr = ''
        for i in range(difficulty):
            checkStr += '0'
        while self.hash[:difficulty] != checkStr:
            self.nonce += 1
            self.hash = self.calculateHash()
        print('Nonce is ' + str(self.nonce))
        print('Hash is ' + self.hash)