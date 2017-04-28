import sqlite3
import time
import datetime

dbName = "Database\\database.db"

def createDBHistTable():
    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect(dbName)
    
    # Get a cursor object
    cursor = db.cursor()
    
    cursor.execute('''
        CREATE TABLE shelfHistoricSales(id INTEGER PRIMARY KEY, shelfLocation TEX, tpnb TEXT, stockgraph TEXT, timestamp TEXT) ''')
    db.commit()
    
def createDBShelfs():
    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect(dbName)
    
    # Get a cursor object
    cursor = db.cursor()
    
    cursor.execute('''
        CREATE TABLE shelfGridTable(id INTEGER PRIMARY KEY, shelfLocation TEXT, TPNB TEXT, 
            unitsOfStock INTEGER, percentageFull REAL, USpointscovered INTEGER, PRpointscovered INTEGER, timestamp TEXT, stockgraph TEXT, priorityscore INTEGER) ''')
    db.commit()
    
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
#     a = [
#         ["1L4B", 41, 50.0, 20.0, "5053827141529", 5, 0.8, "", 0],
#         ["2R6A", 41, 50.0, 20.0, "5051140150471", 9, 0.65, "", 0],
#         ["3L5A", 41, 50.0, 20.0, "5010003000131", 5, 0.9, "", 0],
#         ["4L1B", 41, 50.0, 20.0, "5053526716035", 10, 0.9, "", 0],
#         ["4R4B", 41, 50.0, 20.0, "0000010001875", 97, 0.4, "", 0],
#         ["5L2C", 41, 50.0, 20.0, "5053947211041", 14, 0.2, "", 0],
#         ["6L1D", 41, 50.0, 20.0, "5000462416734", 1, 0.1, "", 0],
#         ["7L2B", 41, 50.0, 20.0, "5010024101381", 1, 0.3, "", 0],
#         ["8L2B", 41, 50.0, 20.0, "5012035936631", 1, 0.5, "", 0],
#         ["9L2B", 41, 50.0, 20.0, "5010204427379", 1, 0.6, "", 0],
#         ["10L2B", 41, 50.0, 20.0, "5000209114510", 1, 0.7, "", 0],
#         ["11L2B", 41, 50.0, 20.0, "5000436725589", 1, 0.35, "", 0]      
#         ]
    
    a = [
        ["1L4B", 41, 50.0, 20.0, "5053827141529", 5, 0.8, 0, 0,"", 0]
        ]
    
    for b in a:
    # Insert row 
        cursor.execute('''
            INSERT INTO shelfGridTable(shelfLocation, TPNB, unitsOfStock, percentageFull, USpointscovered, PRpointscovered, timestamp, stockgraph, priorityscore)
                VALUES(?,?,?,?,?,?,?,?,?)''', (b[0], b[4], b[5], b[6], b[7], b[8],timestamp, b[8], b[9]))
        db.commit()    
    
    
    
def printHistDB():
    db = sqlite3.connect(dbName)
    cursor = db.cursor()
    
    cursor.execute('''SELECT * FROM shelfHistoricSales''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        # row[0] returns the first column in the query (name), row[1] returns email column.
        print('{0} : {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2], row[3], row[4]))
    

    a = [
        ["1L4B", 45, 50.0, 20.0, "5053827141529"],
        ["2R6A", 45, 50.0, 20.0, "5051140150471"],
        ["3L5A", 45, 50.0, 20.0, "5010003000131"],
        ["4L1B", 45, 50.0, 20.0, "5053526716035"],
        ["4R4B", 45, 50.0, 20.0, "0000010001875"],
        ["5L2C", 45, 50.0, 20.0, "5053947211041"],
        ["6L1D", 45, 50.0, 20.0, "5000462416734"],
        ["7L2B", 45, 50.0, 20.0, "5010024101381"],
        ["8L2B", 45, 50.0, 20.0, "5012035936631"],
        ["9L2B", 45, 50.0, 20.0, "5010204427379"],
        ["10L2B", 45, 50.0, 20.0, "5000209114510"],
        ["11L2B", 45, 50.0, 20.0, "5000436725589"]      
        ]
     
    print(a[0][0])

#createDBHistTable()
#createDBShelfs()
#printHistDB()