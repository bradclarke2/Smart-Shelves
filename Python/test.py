import sqlite3
import datetime
import time
import CreateDB

#CreateDB.createDB()
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect(CreateDB.dbName)

# Get a cursor object
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE shelfGridTable(id INTEGER PRIMARY KEY, shelfLocation TEXT, TPNB TEXT, 
        unitsOfStock INTEGER, percentageFull REAL, timestamp TEXT) ''')
db.commit()

cursor.execute('''SELECT id, shelfLocation, TPNB, unitsOfStock, percentageFull, timestamp FROM shelfGridTable''')
all_rows = cursor.fetchall()
print("ID: shelfLocation, TPNB, unitsOfStock, percentageFull, timestamp")
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}, {3}, {4}, {5}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))