import Calculations.stockPercentage as stockpercentages
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import time
import datetime
import sqlite3
import CreateDB
from matplotlib import dates

def MakeHeatMap(singleshelf, XYGridList):
    shelfHeight = singleshelf.height
    shelfName = singleshelf.location
    
    Z_dat = []
    i = 2
    while i > -1:
        Ztemp = []
        for j in range(0,3):
            for XYGrid in XYGridList:
                if (XYGrid.xpos == i and XYGrid.ypos == j and XYGrid.shelflocation == shelfName):
                    print("xpos=",XYGrid.xpos,"ypos=",XYGrid.ypos,"loc=",shelfName,"dist=",XYGrid.USdistance,"res=",stockpercentages.USFullness(shelfHeight, XYGrid.USdistance))
                    Ztemp.append(stockpercentages.USFullness(shelfHeight, XYGrid.USdistance))
        i = i - 1
        Z_dat.append(Ztemp)
    
    print(Z_dat)
    
    cMap = ListedColormap(['red', 'yellow', 'green'])
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(Z_dat, cmap=cMap, vmin = 0, vmax = 2)
    
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

    cbar = plt.colorbar(heatmap)
    cbar.ax.get_yaxis().set_ticks([]) 
    for j, lab in enumerate(['$0$','$1$','$2$']):
        if j ==0:
            lab = "Low"
        if j ==1:
            lab = "Medium"
        if j == 2:
            lab = "High"
        cbar.ax.text(1.5, (2 * j + 1) / 6.0, lab, ha='left', va='center')
        
    plt.title("Stock Level - UltraSonic -" + shelfName + timestamp)
    
    plt.xticks([0, 1, 2, 3])
    plt.yticks([0, 1, 2, 3])

    plt.grid()
    
    ax.set_xticklabels(['Left','','','Right'])
    ax.set_yticklabels(['Front','','','Back'])
    
    file_string = "mysite/personal/static/img/UltraSonic" + shelfName + timestamp + ".png"
    fig.savefig(file_string)
    
    plt.cla()
    plt.close('all')
    
    web_string = "img/UltraSonic" + shelfName + timestamp + ".png"
    singleshelf.imglocation = web_string
    
def MakeSalesGraph(singleshelf):
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
        x_reformated = datetime.datetime.strptime(all_rows[a][5], '%Y-%m-%d %H:%M:%S')
        x.append(x_reformated)
        y.append(all_rows[a][3])
        if x_min == 0 or x_reformated < x_min:
            x_min = x_reformated
            #print("new min = ", x_min)
        if x_max == 0 or x_reformated > x_max:
            x_max = x_reformated
            #print("new max = ", x_max)
        
    fig, ax = plt.subplots()
    
    days = dates.DayLocator(interval=1)
    dayfmt = dates.DateFormatter("%d/%m")
    hours = dates.HourLocator(interval=3)
    hourfmt = dates.DateFormatter('%H:%M')
    
    ax.xaxis.set_minor_locator(hours)
    ax.xaxis.set_minor_formatter(hourfmt)
    ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(dayfmt)
     
    ax.plot(x, y, '-', x, y, 'o')
    
    plt.setp(ax.xaxis.get_minorticklabels(), rotation=45)
    
    ax.xaxis.set_tick_params(which='major', pad=30)
    
    file_string = "mysite/personal/static/img/StockHistory-" + singleshelf.location + ".png"
    fig.savefig(file_string)
    
    web_string = "img/StockHistory-" + singleshelf.location + ".png"   
    singleshelf.salesimglocation = web_string
    
    plt.cla()
    plt.close('all')