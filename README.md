# Coding-challenge-from-Revolut: ERC20 token recorder
Extension of the EthereumDB application with the function of tracing all the erc20 tokens and listing their transactions. Database management system: SQLite.

# Design of the database
The steps of implementation is as follows:
## Get logs from every block
Since for all the ERC20 tokens, there is a significant value in their transactions: the //tx['topic']// is equal to //sha3('Transfer(address,address,uint256)')//
#### tx
Variable | Meaning
--- | --- 
**blockNumber** | number of the block the transaction belongs to
**gas**| gas consumed by the transaction
**gasPrice** | number of Wei to be paid per unit of gas for all computatioon costs of this transaction
**input** | the data sent along with the transaction
**transactionIndex** | index of the transaction in the block
**v, r, s** | used to identify the sender; the signature values of the transaction
**contractAddress** | the contract address created, if the transaction was a contract creation, otherwise null
**cumulativeGasUsed** | the sum of **gasUsed** by this transaction and all preceding transactions in the same block
**gasUsed** | the total amount of gas used when this transaction was executed in the block
**logs** | array of log objects, which the transaction has generated
**logsBloom** | the Bloom filter from indexable info (logger address and log topics) contained in each log entry from the receipt of each transaction in the transaction list
**status** | boolean whether the transaction was successfull; false if the EVM (Ethereum Virtual Machine) reverted the transaction
