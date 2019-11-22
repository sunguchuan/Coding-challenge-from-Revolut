import sqlite3 as sq3
conn = sq3.connect("erc_balance.db")
cur = conn.cursor()

# some SQL code, e.g. select first five entries of the table Quick
cur.execute("SELECT * FROM erc LIMIT 10")
a = cur.fetchall() #list of tuples containing all elements of the row
print (a)
cur.execute("SELECT * FROM tx LIMIT 10")
a = cur.fetchall()
print(a)
conn.close()
