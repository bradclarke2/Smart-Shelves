import Calculations.stockPercentage as stockpercentages
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import time
import datetime

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
                    Ztemp.append(stockpercentages.SingleEmptyFull(shelfHeight, XYGrid.distance))
        i = i - 1
        Z_dat.append(Ztemp)
    
<<<<<<< HEAD
    fig = plt.gcf()
    print(fig)
    plt.clim(0,2)   # clamp the color limits
    plt.title("Stock Level - " + ShelfName)
    plt.colorbar(boundaries=[0,1,2], orientation='horizontal')
    plt.xticks([0,1,2])
    plt.yticks([0,1,2])
=======
    print(Z_dat)
>>>>>>> 5d3560457b950ce94444f3aaa16ed8544eb9dd86
    
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
    singleshelf.imglocation = file_string
    fig.savefig(file_string)