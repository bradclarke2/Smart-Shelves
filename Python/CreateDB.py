import sqlite3

dbName = "Database\\database.db"

def createDB():
    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect(dbName)
    
    # Get a cursor object
    cursor = db.cursor()
    
    cursor.execute('''
        CREATE TABLE shelfGridTable(id INTEGER PRIMARY KEY, shelfLocation TEXT, TPNB TEXT, 
            unitsOfStock INTEGER, percentageFull REAL, timestamp TEXT) ''')
    db.commit()