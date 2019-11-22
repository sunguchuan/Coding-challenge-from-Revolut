"""
Author: Aleksandra Sokolowska
for Validity Labs AG
"""
def create_database(cur):
    """ create the schema for the database"""

    tx = """
    CREATE TABLE IF NOT EXISTS tx (
     blockNumber INTEGER,
     blockHash TEXT,
     logIndex INTEGER,
     sender TEXT,
     recipient TEXT,
     amount INTEGER,
     txHash TEXT,
     transactionIndex INTEGER); """

    erc="""
    CREATE TABLE IF NOT EXISTS erc(
     tokenAddress TEXT PRIMARY KEY,
     balance INTEGER); """

    cur.execute(tx)
    cur.execute(erc)

def create_index(cur):
    tx = "CREATE INDEX index_tx ON tx(blockNumber,transactionIndex);"
    erc= "CREATE INDEX index_erc ON erc(tokenAddress);"

    cur.execute(tx)
    cur.execute(erc)

def update_database(cur, table_erc):
    """ write lists of dictionaries into the database"""
    tx= """ INSERT INTO tx VALUES (:block_number, :block_hash, :log_index, :from, :to, :amount, :transaction_hash, :transaction_index); """
    erc=""" INSERT INTO erc VALUES (:token_address, :balance)"""
    for x in table_erc.keys():
        cur.execute(erc,(x,table_erc[x]['balance']))
        cur.executemany(tx,table_erc[x]['transactions'])
