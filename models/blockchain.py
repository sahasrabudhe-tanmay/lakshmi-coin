from models import block

class Blockchain:

    def __init__(self):
        self.chain = [self.getGenesisBlock()]

    def getGenesisBlock(self):
        return block.Block("Genesis Block", "")

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def setLatestBlock(self, block):
        self.lastBlock = block

    def getBlockFromHash(self, hash):
        return self.blockMap[hash]

    def addBlock(self, data):
        previousHash = self.getLatestBlock().hash
        newBlock = block.Block(data, previousHash)
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
        