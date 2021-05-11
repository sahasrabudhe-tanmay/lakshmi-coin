from models import blockchain

chain = blockchain.Blockchain()
print('Blockchain valid - ' + str(chain.isChainValid()))

chain.addBlock({
    "from": "Tanmay Sahasrabudhe",
    "to": "Shannon Dias",
    "amount": 100
})
chain.addBlock({
    "from": "Shannon Dias",
    "to": "Tanmay Sahasrabudhe",
    "amount": 50
})

print('Blockchain valid - ' + str(chain.isChainValid()))