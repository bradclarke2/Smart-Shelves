import matplotlib 
matplotlib.use("TkAgg")
import Calculations.stockPercentage as stockpercentages
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import time
import datetime
import sqlite3
import CreateDB
from matplotlib import dates
import os
import time



def MakeHeatMap(singleshelf, XYGridList):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    print ("before heatmap ",timestamp)
    
    shelfHeight = singleshelf.height
    shelfName = singleshelf.location
    
    Z_dat = []
    i = 2
    while i > -1:
        Ztemp = []
        for j in range(0,3):
            for XYGrid in XYGridList:
                if (XYGrid.xpos == i and XYGrid.ypos == j and XYGrid.shelflocation == shelfName):
                    Ztemp.append(stockpercentages.USFullness(shelfHeight, XYGrid.USdistance))
        i = i - 1
        Z_dat.append(Ztemp)
    
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
    
    file_string = os.path.dirname("mysite/personal/static/img/UltraSonic" + shelfName + timestamp + ".png")+"/UltraSonic" + shelfName + timestamp + ".png"
    fig.savefig(file_string, transparent=True)
    
    plt.cla()
    plt.close('all')
    
    web_string = "img/UltraSonic" + shelfName + timestamp + ".png"
    singleshelf.imglocation = web_string
    
def MakeSalesGraph(singleshelf):
    print("makingsalesgrapg")
    
    file_string = os.path.dirname("mysite/graph/static/img/StockHistory-"+singleshelf.location+".png") + "/StockHistory-"+singleshelf.location+".png"
    #try:
    #   print("trying")
    #os.remove(file_string)
    #print("success")
    #except OSError:
    #    print("fail")
    #    pass
    #time.sleep(5)
    plt.clf()
    
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
        if x_max == 0 or x_reformated > x_max:
            x_max = x_reformated
        
    fig, ax = plt.subplots()
    
    days = dates.DayLocator(interval=1)
    dayfmt = dates.DateFormatter("%d/%m")
    hours = dates.HourLocator(interval=3)
    hourfmt = dates.DateFormatter('%H:%M')
    
    ax.xaxis.set_minor_locator(hours)
    ax.xaxis.set_minor_formatter(hourfmt)
    ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(dayfmt)
     
    lines = ax.plot(x, y, 'o', x, y, '-')
    

    
    plt.setp(ax.xaxis.get_minorticklabels(), rotation=45)
    
    ax.xaxis.set_tick_params(which='major', pad=30)
    lines.pop(0).remove()
    
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    
    file_string2 = "mysite/graph/static/img/StockHistory-"+singleshelf.location+timestamp+".png"
    web_string = "img/StockHistory-" + singleshelf.location + timestamp + ".png"   
    singleshelf.salesimglocation = web_string   
    fig.savefig(file_string2, transparent=True)
    #plt.savefig(file_string2, transparent=True)
    
    # Creates or opens a file called mydb with a SQLite3 DB  

    cursor.execute('''INSERT INTO shelfHistoricSales(shelfLocation, tpnb, stockgraph, timestamp)
                      VALUES(?,?,?,?)''', (singleshelf.location, singleshelf.tpnb, web_string, timestamp))
    db.commit()
    
    plt.clf()