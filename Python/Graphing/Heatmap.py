import Calculations.stockPercentage as stockpercentages
import matplotlib.pyplot as plt

def MakeHeatMap(shelfHeight, XYGridList, ShelfName):
    Z_dat = []
    
    for i in range(0,3):
        Ztemp = []
        for j in range(0,3):
            for XYGrid in XYGridList:
                if (XYGrid.xpos == i and XYGrid.ypos == j and XYGrid.shelflocation == ShelfName):
                    Ztemp.append(stockpercentages.SingleEmptyFull(shelfHeight, XYGrid.distance))
        Z_dat.append(Ztemp)
        
    p = plt.imshow(Z_dat, cmap="RdYlGn")    
    
    fig = plt.gcf()
    print(fig)
    plt.clim(0,2)   # clamp the color limits
    plt.title("Stock Level - " + ShelfName)
    plt.colorbar(boundaries=[0,1,2], orientation='horizontal')
    plt.xticks([0,1,2])
    plt.yticks([0,1,2])
    
    fig.savefig("mysite/personal/static/img/" + ShelfName + ".png")
    
    plt.close()  

    #plt.show()