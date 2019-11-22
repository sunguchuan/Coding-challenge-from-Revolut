
def parse_erc20(web3,tx,source,to,val):
    erc_table={}
    erc_table['block_hash']=web3.toHex(tx['blockHash'])
    erc_table['from']=source
    erc_table['to']=to
    erc_table['amount']=val
    erc_table['block_number']=tx['blockNumber']
    erc_table['log_index']=tx['logIndex']
    erc_table['transaction_hash']=web3.toHex(tx['transactionHash'])
    erc_table['transaction_index']=tx['transactionIndex']

    return erc_table

def execute_sql(table_erc):
    import os
    from sql_helper import create_database, update_database, create_index
    import sqlite3 as sq3

    db_name = 'erc_balance.db'
    db_is_new = not os.path.exists(db_name)

    #connect to the database
    conn = sq3.connect(db_name) # or use :memory: to put it in RAM
    cur = conn.cursor()

    if db_is_new:
        print('Creating a new DB.')
        create_database(cur)
        create_index(cur)
        update_database(cur,table_erc)
    else:
        update_database(cur,table_erc)
    conn.commit()
    conn.close()
