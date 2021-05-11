from models import block
import time

class Blockchain:

    def __init__(self):
        self.chain = [self.getGenesisBlock()]
        self.difficulty = 5

    def getGenesisBlock(self):
        return block.Block("Genesis Block", "", time.time_ns())

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def setLatestBlock(self, block):
        self.lastBlock = block

    def getBlockFromHash(self, hash):
        return self.blockMap[hash]

    def addBlock(self, data):
        previousHash = self.getLatestBlock().hash
        newBlock = block.Block(data, previousHash, time.time_ns())
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False
        return True
        