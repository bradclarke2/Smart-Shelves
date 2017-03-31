import sqlite3
import Objects.shelf as ShelfObject
import CreateDB
import matplotlib.pyplot as plt
import time
from matplotlib import dates
from datetime import datetime
import InsertDB

ShelfList = ShelfObject.makeShelfGrid()

singleshelf = ShelfList[1]
print(singleshelf.location)

InsertDB.insertShelfRecord(singleshelf)

db = sqlite3.connect(CreateDB.dbName)
cursor = db.cursor()
cursor.execute("SELECT * FROM shelfGridTable WHERE shelfLocation = (?)", (singleshelf.location,))

all_rows = cursor.fetchall()
i = len(all_rows)

x = []
y = []

x_min = 0
x_max = 0

for a in range (0, i): 
    x_reformated = datetime.strptime(all_rows[a][5], '%Y-%m-%d %H:%M:%S')
    x.append(x_reformated)
    y.append(all_rows[a][3])
    if x_min == 0 or x_reformated < x_min:
        x_min = x_reformated
        print("new min = ", x_min)
    if x_max == 0 or x_reformated > x_max:
        x_max = x_reformated
        print("new max = ", x_max)
    
fig, ax = plt.subplots()

days = dates.DayLocator(interval=1)
dayfmt = dates.DateFormatter("%d/%m")
hours = dates.HourLocator(interval=3)
hourfmt = dates.DateFormatter('%H:%M')

ax.xaxis.set_minor_locator(hours)
ax.xaxis.set_minor_formatter(hourfmt)
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(dayfmt)

datemin = datetime.date(x_min)
datemax = datetime.date(x_max)
ax.set_xlim(datemin, datemax)

ax.plot(x, y, '-', x, y, 'o')

plt.setp(ax.xaxis.get_minorticklabels(), rotation=45)

ax.xaxis.set_tick_params(which='major', pad=30)

plt.show()