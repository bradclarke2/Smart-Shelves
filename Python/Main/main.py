import serial
import time
from Calculations.stockPercentage import checkStock
import matplotlib.pyplot as plt
        
class XYGrid(object):
    """__init__() functions as the class constructor"""

    def __init__(self, idpos=None, xpos = None, ypos = None, distance = None):
        self.idpos = idpos
        self.xpos = xpos
        self.ypos = ypos
        self.distance = distance
               
def MeasureDistance(XYGridList):
    ser = serial.Serial('COM9')
    ser.readline()
    time.sleep(2)
    waiter = 1
    while waiter == 1:
        line = str(ser.readline(),'utf-8')
        line = line.strip("\r\n")
        listData = line.split(",")    
        print("line=",listData)
        
        listData = [float(i) for i in listData]
        
        for XYGrid in XYGridList:
            XYGrid.distance = listData[XYGrid.idpos]
            print("id=",XYGrid.idpos,"dist=",XYGrid.distance)
        waiter = 0           

def MakeHeatMap(XYGridList):
    Z_dat = []
    
    for i in range(0,3):
        Ztemp = []
        for j in range(0,3):
            for XYGrid in XYGridList:
                if (XYGrid.xpos == i and XYGrid.ypos == j):
                    Ztemp.append(XYGrid.distance)
        Z_dat.append(Ztemp)
    
    for i in range(5):
        if i == 0:
            p = plt.imshow(Z_dat)
            fig = plt.gcf()
            plt.clim()   # clamp the color limits
            plt.title("Boring slide show")
            plt.colorbar()  
        else:
            p.set_data(Z_dat)
    
        print("step", i)
        plt.pause(0.5)

XYGridList = []
XYGridList.append(XYGrid(0, 0, 0, 0.00))
XYGridList.append(XYGrid(1, 0, 1, 0.00))
XYGridList.append(XYGrid(2, 0, 2, 0.00)) 
XYGridList.append(XYGrid(3, 1, 0, 0.00))
XYGridList.append(XYGrid(4, 1, 1, 0.00))
XYGridList.append(XYGrid(5, 1, 2, 0.00))
XYGridList.append(XYGrid(6, 2, 0, 0.00))
XYGridList.append(XYGrid(7, 2, 1, 0.00))
XYGridList.append(XYGrid(8, 2, 2, 0.00))  

MeasureDistance(XYGridList)
MakeHeatMap(XYGridList)

stockLevel = checkStock(XYGrid, XYGridList)
print(stockLevel)