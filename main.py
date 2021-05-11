from models.transaction import Transaction
from models.blockchain import Blockchain

chain = Blockchain()
chain.createTransaction(Transaction('Shannon', 'Tanmay', 100))
chain.createTransaction(Transaction('Tanmay', 'Shannon', 50))

chain.minePendingTransaction('Tanmay')
print('Balance of Tanmay is ' + str(chain.getBalanceOfUser('Tanmay')))