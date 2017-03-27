import Calculations.stockPercentage as stockpercentages
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

def MakeHeatMap(shelfHeight, XYGridList, ShelfName):
    Z_dat = []
    i = 2
    while i > -1:
        Ztemp = []
        for j in range(0,3):
            for XYGrid in XYGridList:
                if (XYGrid.xpos == i and XYGrid.ypos == j and XYGrid.shelflocation == ShelfName):
                    Ztemp.append(stockpercentages.SingleEmptyFull(shelfHeight, XYGrid.distance))
        i = i - 1
        Z_dat.append(Ztemp)
    
    print(Z_dat)
    
    cMap = ListedColormap(['red', 'yellow', 'green'])
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(Z_dat, cmap=cMap, vmin = 0, vmax = 2)


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
        
    plt.title("Stock Level - UltraSound -" + ShelfName)
    
    plt.xticks([0, 1, 2, 3])
    plt.yticks([0, 1, 2, 3])

    plt.grid()
    
    ax.set_xticklabels(['Left','','','Right'])
    ax.set_yticklabels(['Front','','','Back'])
    fig.savefig("mysite/personal/static/img/UltraSound" + ShelfName + ".png")