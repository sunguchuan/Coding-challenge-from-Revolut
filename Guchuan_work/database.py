"""
Author: Aleksandra Sokolowska
for Validity Labs AG
"""

from web3 import Web3
from organize import *
import sys
import time
import json

#uncomment one of the options below
# 1. connection via Infura
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/ba1c59965f3341d581b8e0284afda3f7"))

# 2. or connection via local node
#web3 = Web3(Web3.IPCProvider('/your-path-to/geth.ipc'))

user=sys.argv[1]
start_time = time.time()

start=8974000
tokens={}

output_every=100
count=0
#loop over all blocks
erc_topic='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
with open('erc.json','r')as f:
    erc_abi=json.load(f)

latest_bk=web3.eth.getBlock('latest')
latest=latest_bk['number']
erc_data=None
# test
latest=8974371
while start<latest:

    filter={'fromBlock':latest-20,'toBlock':latest,'topics':[erc_topic]}

    erc_data=web3.eth.getLogs(filter)
    user_address=web3.toChecksumAddress(user)
    for tx in erc_data:
        if len(tx['topics'])>1:
            from_address=web3.toHex(tx['topics'][1])
            from_address='0x'+from_address[26:]
            to_address=web3.toHex(tx['topics'][2])
            to_address='0x'+to_address[26:]
            if len(tx['topics'])==3:
                amount=web3.toInt(hexstr=tx['data'])
            else:
                amount=web3.toHex(tx['topics'][3])
                amount=web3.toInt(hexstr=amount)
        else:
            from_address='0x'+tx['data'][26:66]
            to_address='0x'+tx['data'][90:130]
            amount=web3.toInt(hexstr=tx['data'][130:])

        from_address=web3.toChecksumAddress(from_address)
        to_address=web3.toChecksumAddress(to_address)

        if from_address==user_address or to_address==user_address:
            token_address=tx['address']
            token_address=web3.toChecksumAddress(token_address)
            contract=web3.eth.contract(address=token_address,abi=erc_abi)
            balance=contract.functions.balanceOf(user_address).call()
            if balance!=0 and token_address not in tokens:
                account={'balance':balance,'transactions':[]}
                tokens[token_address]=account
            tokens[token_address]['transactions'].append(parse_erc20(web3,tx,from_address,to_address,amount))
            print(tokens)
    print(latest)
    latest-=20  # Some blocks has too many entries that leads the error of more than 10000 entries
execute_sql(tokens)
