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
    
def insertDBShelfs():
    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect(dbName)
    # Get a cursor object
    cursor = db.cursor()
#         ]
    
    a = [
        
        
        ["2R6A","5051140150471",40,1,8,8,"2017-04-30 18:11:15","",100],
        ["2R6A","5051140150471",36,0.9,8,8,"2017-04-30 22:11:15","",100],
        ["2R6A","5051140150471",35.6,0.89,8,8,"2017-05-01 02:11:15","",100],
        ["2R6A","5051140150471",28.8,0.72,8,8,"2017-05-01 06:11:15","",100],
        ["2R6A","5051140150471",40,1,8,8,"2017-05-01 10:11:15","",100],
        ["2R6A","5051140150471",31.6,0.79,8,8,"2017-05-01 14:11:15","",100],
        ["2R6A","5051140150471",22.4,0.56,8,8,"2017-05-01 18:11:15","",100],
        ["2R6A","5051140150471",16,0.4,8,8,"2017-05-01 22:11:15","",100],
        ["2R6A","5051140150471",10,0.25,8,8,"2017-05-02 02:11:15","",100],
        ["2R6A","5051140150471",2,0.05,8,8,"2017-05-02 06:11:15","",100],
        ["2R6A","5051140150471",0,0,8,8,"2017-05-02 10:11:15","",100],
        ["2R6A","5051140150471",38.4,0.96,8,8,"2017-05-02 14:11:15","",100],
        ["3L5A","5010003000131",0,0,8,8,"2017-04-30 18:11:15","",100],
        ["3L5A","5010003000131",0,0,8,8,"2017-04-30 22:11:15","",100],
        ["3L5A","5010003000131",38,0.95,8,8,"2017-05-01 02:11:15","",100],
        ["3L5A","5010003000131",28,0.7,8,8,"2017-05-01 06:11:15","",100],
        ["3L5A","5010003000131",18,0.45,8,8,"2017-05-01 10:11:15","",100],
        ["3L5A","5010003000131",8,0.2,8,8,"2017-05-01 14:11:15","",100],
        ["3L5A","5010003000131",0,0,8,8,"2017-05-01 18:11:15","",100],
        ["3L5A","5010003000131",0,0,8,8,"2017-05-01 22:11:15","",100],
        ["3L5A","5010003000131",0,0,8,8,"2017-05-02 02:11:15","",100],
        ["3L5A","5010003000131",39.6,0.99,8,8,"2017-05-02 06:11:15","",100],
        ["3L5A","5010003000131",36,0.9,8,8,"2017-05-02 10:11:15","",100],
        ["3L5A","5010003000131",35.2,0.88,8,8,"2017-05-02 14:11:15","",100],
        ["4L1B","5053526716035",40,1,8,8,"2017-04-30 18:11:15","",100],
        ["4L1B","5053526716035",40,1,8,8,"2017-04-30 22:11:15","",100],
        ["4L1B","5053526716035",40,1,8,8,"2017-05-01 02:11:15","",100],
        ["4L1B","5053526716035",38,0.95,8,8,"2017-05-01 06:11:15","",100],
        ["4L1B","5053526716035",36,0.9,8,8,"2017-05-01 10:11:15","",100],
        ["4L1B","5053526716035",32,0.8,8,8,"2017-05-01 14:11:15","",100],
        ["4L1B","5053526716035",29.6,0.74,8,8,"2017-05-01 18:11:15","",100],
        ["4L1B","5053526716035",28.8,0.72,8,8,"2017-05-01 22:11:15","",100],
        ["4L1B","5053526716035",28.4,0.71,8,8,"2017-05-02 02:11:15","",100],
        ["4L1B","5053526716035",28.4,0.71,8,8,"2017-05-02 06:11:15","",100],
        ["4L1B","5053526716035",39.2,0.98,8,8,"2017-05-02 10:11:15","",100],
        ["4L1B","5053526716035",38.4,0.96,8,8,"2017-05-02 14:11:15","",100],
        ["4R4B","0000010001875",0,0,8,8,"2017-04-30 18:11:15","",100],
        ["4R4B","0000010001876",40,1,8,8,"2017-04-30 22:11:15","",100],
        ["4R4B","0000010001877",38.4,0.96,8,8,"2017-05-01 02:11:15","",100],
        ["4R4B","0000010001878",37.6,0.94,8,8,"2017-05-01 06:11:15","",100],
        ["4R4B","0000010001879",24,0.6,8,8,"2017-05-01 10:11:15","",100],
        ["4R4B","0000010001880",21.6,0.54,8,8,"2017-05-01 14:11:15","",100],
        ["4R4B","0000010001881",40,1,8,8,"2017-05-01 18:11:15","",100],
        ["4R4B","0000010001882",36,0.9,8,8,"2017-05-01 22:11:15","",100],
        ["4R4B","0000010001883",34,0.85,8,8,"2017-05-02 02:11:15","",100],
        ["4R4B","0000010001884",40,1,8,8,"2017-05-02 06:11:15","",100],
        ["4R4B","0000010001885",30,0.75,8,8,"2017-05-02 10:11:15","",100],
        ["4R4B","0000010001886",40,1,8,8,"2017-05-02 14:11:15","",100],
        ["5L2C","5053947211041",40,1,8,8,"2017-04-30 18:11:15","",100],
        ["5L2C","5053947211041",36,0.9,8,8,"2017-04-30 22:11:15","",100],
        ["5L2C","5053947211041",32,0.8,8,8,"2017-05-01 02:11:15","",100],
        ["5L2C","5053947211041",28,0.7,8,8,"2017-05-01 06:11:15","",100],
        ["5L2C","5053947211041",24,0.6,8,8,"2017-05-01 10:11:15","",100],
        ["5L2C","5053947211041",20,0.5,8,8,"2017-05-01 14:11:15","",100],
        ["5L2C","5053947211041",8,0.2,8,8,"2017-05-01 18:11:15","",100],
        ["5L2C","5053947211041",0,0,8,8,"2017-05-01 22:11:15","",100],
        ["5L2C","5053947211041",0,0,8,8,"2017-05-02 02:11:15","",100],
        ["5L2C","5053947211041",0,0,8,8,"2017-05-02 06:11:15","",100],
        ["5L2C","5053947211041",40,1,8,8,"2017-05-02 10:11:15","",100],
        ["5L2C","5053947211041",32,0.8,8,8,"2017-05-02 14:11:15","",100],
        ["6L1D","5000462416734",16,0.4,8,8,"2017-04-30 18:11:15","",100],
        ["6L1D","5000462416734",8,0.2,8,8,"2017-04-30 22:11:15","",100],
        ["6L1D","5000462416734",6,0.15,8,8,"2017-05-01 02:11:15","",100],
        ["6L1D","5000462416734",40,1,8,8,"2017-05-01 06:11:15","",100],
        ["6L1D","5000462416734",34.8,0.87,8,8,"2017-05-01 10:11:15","",100],
        ["6L1D","5000462416734",16,0.4,8,8,"2017-05-01 14:11:15","",100],
        ["6L1D","5000462416734",8,0.2,8,8,"2017-05-01 18:11:15","",100],
        ["6L1D","5000462416734",0.4,0.01,8,8,"2017-05-01 22:11:15","",100],
        ["6L1D","5000462416734",0,0,8,8,"2017-05-02 02:11:15","",100],
        ["6L1D","5000462416734",0,0,8,8,"2017-05-02 06:11:15","",100],
        ["6L1D","5000462416734",0,0,8,8,"2017-05-02 10:11:15","",100],
        ["6L1D","5000462416734",40,1,8,8,"2017-05-02 14:11:15","",100],
        ["7L2B","5010024101381",30,0.75,8,8,"2017-04-30 18:11:15","",100],
        ["7L2B","5010024101381",40,1,8,8,"2017-04-30 22:11:15","",100],
        ["7L2B","5010024101381",32,0.8,8,8,"2017-05-01 02:11:15","",100],
        ["7L2B","5010024101381",26.8,0.67,8,8,"2017-05-01 06:11:15","",100],
        ["7L2B","5010024101381",16,0.4,8,8,"2017-05-01 10:11:15","",100],
        ["7L2B","5010024101381",8,0.2,8,8,"2017-05-01 14:11:15","",100],
        ["7L2B","5010024101381",6,0.15,8,8,"2017-05-01 18:11:15","",100],
        ["7L2B","5010024101381",6,0.15,8,8,"2017-05-01 22:11:15","",100],
        ["7L2B","5010024101381",5.2,0.13,8,8,"2017-05-02 02:11:15","",100],
        ["7L2B","5010024101381",4.8,0.12,8,8,"2017-05-02 06:11:15","",100],
        ["7L2B","5010024101381",4,0.1,8,8,"2017-05-02 10:11:15","",100],
        ["7L2B","5010024101381",3.2,0.08,8,8,"2017-05-02 14:11:15","",100],
        ["8L2B","5012035936631",40,1,8,8,"2017-04-30 18:11:15","",100],
        ["8L2B","5012035936631",40,1,8,8,"2017-04-30 22:11:15","",100],
        ["8L2B","5012035936631",40,1,8,8,"2017-05-01 02:11:15","",100],
        ["8L2B","5012035936631",40,1,8,8,"2017-05-01 06:11:15","",100],
        ["8L2B","5012035936631",40,1,8,8,"2017-05-01 10:11:15","",100],
        ["8L2B","5012035936631",40,1,8,8,"2017-05-01 14:11:15","",100],
        ["8L2B","5012035936631",40,1,8,8,"2017-05-01 18:11:15","",100],
        ["8L2B","5012035936631",38,0.95,8,8,"2017-05-01 22:11:15","",100],
        ["8L2B","5012035936631",36,0.9,8,8,"2017-05-02 02:11:15","",100],
        ["8L2B","5012035936631",35.2,0.88,8,8,"2017-05-02 06:11:15","",100],
        ["8L2B","5012035936631",28.8,0.72,8,8,"2017-05-02 10:11:15","",100],
        ["8L2B","5012035936631",40,1,8,8,"2017-05-02 14:11:15","",100],
        ["9L2B","5010204427379",40,1,8,8,"2017-04-30 18:11:15","",100],
        ["9L2B","5010204427379",38.4,0.96,8,8,"2017-04-30 22:11:15","",100],
        ["9L2B","5010204427379",28.8,0.72,8,8,"2017-05-01 02:11:15","",100],
        ["9L2B","5010204427379",21.2,0.53,8,8,"2017-05-01 06:11:15","",100],
        ["9L2B","5010204427379",40,1,8,8,"2017-05-01 10:11:15","",100],
        ["9L2B","5010204427379",30.4,0.76,8,8,"2017-05-01 14:11:15","",100],
        ["9L2B","5010204427379",22.8,0.57,8,8,"2017-05-01 18:11:15","",100],
        ["9L2B","5010204427379",14,0.35,8,8,"2017-05-01 22:11:15","",100],
        ["9L2B","5010204427379",40,1,8,8,"2017-05-02 02:11:15","",100],
        ["9L2B","5010204427379",28,0.7,8,8,"2017-05-02 06:11:15","",100],
        ["9L2B","5010204427379",20,0.5,8,8,"2017-05-02 10:11:15","",100],
        ["9L2B","5010204427379",8,0.2,8,8,"2017-05-02 14:11:15","",100],
        ["10L2B","5000209114510",40,1,8,8,"2017-04-30 18:11:15","",100],
        ["10L2B","5000209114510",40,1,8,8,"2017-04-30 22:11:15","",100],
        ["10L2B","5000209114510",38,0.95,8,8,"2017-05-01 02:11:15","",100],
        ["10L2B","5000209114510",36,0.9,8,8,"2017-05-01 06:11:15","",100],
        ["10L2B","5000209114510",20,0.5,8,8,"2017-05-01 10:11:15","",100],
        ["10L2B","5000209114510",12,0.3,8,8,"2017-05-01 14:11:15","",100],
        ["10L2B","5000209114510",8,0.2,8,8,"2017-05-01 18:11:15","",100],
        ["10L2B","5000209114510",40,1,8,8,"2017-05-01 22:11:15","",100],
        ["10L2B","5000209114510",39.6,0.99,8,8,"2017-05-02 02:11:15","",100],
        ["10L2B","5000209114510",30.4,0.76,8,8,"2017-05-02 06:11:15","",100],
        ["10L2B","5000209114510",20,0.5,8,8,"2017-05-02 10:11:15","",100],
        ["10L2B","5000209114510",10,0.25,8,8,"2017-05-02 14:11:15","",100],
        ["11L2B","5000436725589",0,0,8,8,"2017-04-30 18:11:15","",100],
        ["11L2B","5000436725589",0,0,8,8,"2017-04-30 22:11:15","",100],
        ["11L2B","5000436725589",0,0,8,8,"2017-05-01 02:11:15","",100],
        ["11L2B","5000436725589",0,0,8,8,"2017-05-01 06:11:15","",100],
        ["11L2B","5000436725589",40,1,8,8,"2017-05-01 10:11:15","",100],
        ["11L2B","5000436725589",36,0.9,8,8,"2017-05-01 14:11:15","",100],
        ["11L2B","5000436725589",32,0.8,8,8,"2017-05-01 18:11:15","",100],
        ["11L2B","5000436725589",26,0.65,8,8,"2017-05-01 22:11:15","",100],
        ["11L2B","5000436725589",1.2,0.03,8,8,"2017-05-02 02:11:15","",100],
        ["11L2B","5000436725589",40,1,8,8,"2017-05-02 06:11:15","",100],
        ["11L2B","5000436725589",29.6,0.74,8,8,"2017-05-02 10:11:15","",100],
        ["11L2B","5000436725589",24.8,0.62,8,8,"2017-05-02 14:11:15","",100]

        
           
        ]
    for b in a:
    # Insert row 
        cursor.execute('''
            INSERT INTO shelfGridTable(shelfLocation, TPNB, unitsOfStock, percentageFull, USpointscovered, PRpointscovered, timestamp, stockgraph, priorityscore)
                VALUES(?,?,?,?,?,?,?,?,?)''', (b[0], b[1], b[2], b[3], b[4], b[5],b[6], b[7], b[8]))
        db.commit()  
    
def printHistDB():
    db = sqlite3.connect(dbName)
    cursor = db.cursor()
    
    cursor.execute('''SELECT * FROM shelfGridTable''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        # row[0] returns the first column in the query (name), row[1] returns email column.
        #print('{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        print(row)
    


# createDBHistTable()
# createDBShelfs()
# insertDBShelfs()
# printHistDB()

