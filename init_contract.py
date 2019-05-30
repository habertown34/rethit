from web3 import Web3

web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545")) # set Web3Provider

# open contract binary file
contract_file = open('c:/dev/py/web3/build/Rethit.bin')
contract_bytecode = contract_file.readline()
contract_file.close()

# open abi file
abi_file = open('c:/dev/py/web3/build/rethit-abi.json')
abi = abi_file.read()
abi_file.close()

rethit = web3.eth.contract(bytecode=contract_bytecode, abi=abi) # make contract object
web3.eth.defaultAccount = web3.eth.accounts[0] # set account
tx_hash = rethit.constructor().transact() # deploy contract
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash) # wait for receipt to be mined

# print contract address
print('Contract address:')
print(tx_receipt.contractAddress)