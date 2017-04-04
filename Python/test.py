########### Python 3.2 #############
# import http.client, urllib.request, urllib.parse, urllib.error, base64
# import json
# 
# headers = {
#     # Request headers
#     'Ocp-Apim-Subscription-Key': '5c5d3ac3d5a9414face805ad31bc13b5',
# }
# 
# params = urllib.parse.urlencode({
#     # Request parameters
#     'tpnb': '054550994',
# 
# })
# 
# try:
#     conn = http.client.HTTPSConnection('dev.tescolabs.com')
#     conn.request("GET", "/product/?%s" % params, "{body}", headers)
#     response = conn.getresponse()
#     data = response.read()
#     print(data)
#     conn.close()
#     parsed_data = json.loads(data)
#     description = parsed_data['products'][0]['description']
#     print(description)
#     
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))

import sqlite3

dbName = "Database\\database.db"


# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect(dbName)

# Get a cursor object
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE shelfGridTable(id INTEGER PRIMARY KEY, shelfLocation TEXT, TPNB TEXT, 
        unitsOfStock INTEGER, percentageFull REAL, timestamp TEXT) ''')
db.commit()

