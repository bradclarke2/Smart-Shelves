<<<<<<< HEAD
import sqlite3

dbName = "Database\\database.db"

def createDB():
    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect(dbName)
    
    # Get a cursor object
    cursor = db.cursor()
    
    cursor.execute('''
        CREATE TABLE shelfGridTable(id INTEGER PRIMARY KEY, shelfLocation TEXT, TPNB TEXT, 
            unitsOfStock INTEGER, percentageFull REAL, timestamp TEXT, stockgraph TEXT, priorityscore INTEGER) ''')
    db.commit()
    
createDB()
=======
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('example.ini')

key = parser.get('credentials', 'APIkey')
print(key)
>>>>>>> e05e9cfa9027e2f506f9de394851179579bcd6b9
