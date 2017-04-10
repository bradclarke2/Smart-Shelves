import sqlite3
import datetime
import time
import CreateDB

def insertShelfRecord(singleshelf):
    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect(CreateDB.dbName)
    cursor = db.cursor()
    
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
     
    # Insert row 
    cursor.execute('''INSERT INTO shelfGridTable(shelfLocation, TPNB, unitsOfStock, percentageFull, timestamp, stockgraph, priorityscore)
                      VALUES(?,?,?,?,?,?,?)''', (singleshelf.location, singleshelf.tpnb, singleshelf.unitsOccupied, singleshelf.volumePercentFull, timestamp, singleshelf.salesimglocation, singleshelf.priorityscore))
    db.commit()

def printShelfDB():
    db = sqlite3.connect(CreateDB.dbName)
    cursor = db.cursor()
    
    cursor.execute('''SELECT id, shelfLocation, TPNB, unitsOfStock, percentageFull, timestamp, stockgraph, priorityscore FROM shelfGridTable''')
    all_rows = cursor.fetchall()
    print("ID: shelfLocation, TPNB, unitsOfStock, percentageFull, timestamp, stock graph, priorityscore")
    for row in all_rows:
        # row[0] returns the first column in the query (name), row[1] returns email column.
        print('{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))