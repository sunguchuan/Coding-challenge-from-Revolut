# Coding-challenge-from-Revolut: ERC20 token recorder
Extension of the EthereumDB application with the function of tracing all the erc20 tokens and listing their transactions. Database management system: SQLite.

# Design of the database
The steps of implementation is as follows:
## Get logs from every block
Since for all the ERC20 tokens, there is a significant value in their transactions: the `tx['topic']` is equal to `sha3('Transfer(address,address,uint256)')`. Based on this fact, the filter is set to retrieve all the logs with such value in their `topic` fields. Initially, a dictionary is allocated with the key of the token's address. The application goes through the blockchain from the latest one to the first. If there is a log found by the filter, it is an ERC20 transaction. If the transaction is from or to the given `user_address`, it means we need to add this transaction to the database. If the token's address cannot be found in the dictionary, we need to search the address and get the balance of the `user_address` by using the `balanceOf()` call and the ERC20 abi. The application maps the balance and the list of transactions to the token's address and after searching some blocks, it creates or updates the `tx` and `erc` tables.

#### tx
Variable | Meaning
--- | --- 
**blockNumber** | number of the block the transaction belongs to
**blockHash**| hash value of the block storing the transaction
**logIndex** | index of the log in the block
**sender** | the source of the erc20 token comes from in the transaction
**recipient** | the destination where the transferred token goes to
**amount** | the number of erc20 tokens transferred
**txHash** | hash value of the transaction storing the log
**transactionIndex** | index of the transaction in the block

#### erc
Variable | Meaning
--- | --- 
**tokenAddress** | contract address of the erc20 token
**balance**| the balance of `user_address`

The test method is similar to the reference [here](https://github.com/validitylabs/EthereumDB/blob/master).
you may run `python3 test_data.py` under the folder's directory.
Here is a result of test code:
[](Guchuan_work/test_result.png)
