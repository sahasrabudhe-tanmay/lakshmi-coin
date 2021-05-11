from models.transaction import Transaction
from models.block import Block
import time

class Blockchain:

    def __init__(self):
        self.chain = [self.getGenesisBlock()]
        self.difficulty = 4
        self.pendingTransactions = []
        self.miningReward = 100

    def getGenesisBlock(self):
        return Block([Transaction('admin-rewards', 'Tanmay', 100)], '', time.time_ns())

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def minePendingTransaction(self, rewardAdress):
        lastBlock = self.getLatestBlock()
        newBlock = Block(self.pendingTransactions, lastBlock.hash, time.time_ns())
        newBlock.mineBlock(self.difficulty)

        print('Block mined successfully')
        self.chain.append(newBlock)
        self.pendingTransactions = [
            Transaction('admin-rewards', rewardAdress, self.miningReward)
        ]

    def createTransaction(self, transaction: Transaction):
        self.pendingTransactions.append(transaction)

    def getBalanceOfUser(self, key):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.senderKey == key:
                    balance -= transaction.amount
                if transaction.receiverKey == key:
                    balance += transaction.amount
        return balance

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False
        return True
        