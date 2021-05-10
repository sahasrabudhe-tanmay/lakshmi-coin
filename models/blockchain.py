from models import block

class Blockchain:

    def __init__(self):
        self.lastBlock = self.getGenesisBlock()
        self.blockMap = {
            self.lastBlock.hash: self.lastBlock
        }

    def getGenesisBlock(self):
        return block.Block("Genesis Block", "")

    def getLatestBlock(self):
        return self.lastBlock

    def setLatestBlock(self, block):
        self.lastBlock = block

    def getBlockFromHash(self, hash):
        return self.blockMap[hash]

    def addBlock(self, data):
        previousHash = self.getLatestBlock().hash
        newBlock = block.Block(data, previousHash)
        self.setLatestBlock(newBlock)
        self.blockMap[newBlock.hash] = newBlock

    def isChainValid(self):
        i = 1
        currentBlock = self.getLatestBlock()
        while currentBlock.previousHash != "":
            previousBlock = self.getBlockFromHash(currentBlock.previousHash)
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False
            currentBlock = self.getBlockFromHash(currentBlock.previousHash)
            i += 1
        if i != len(self.blockMap):
            return False
        return True
        