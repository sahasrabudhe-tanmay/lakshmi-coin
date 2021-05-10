import time
import hashlib

class Block:

    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.timestamp = time.time_ns()
        self.hash = self.calculateHash()
        
    def calculateHash(self):
        return hashlib.sha256(str(self.data).encode('utf-8') + self.previousHash.encode('utf-8') + str(self.timestamp).encode('utf-8')).hexdigest()

        