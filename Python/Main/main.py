import serial
import time
from Calculations.stockPercentage import checkStock
        
class XYGrid(object):
    """__init__() functions as the class constructor"""

    def __init__(self, idpos=None, xpos = None, ypos = None, distance = None):
        self.idpos = idpos
        self.xpos = xpos
        self.ypos = ypos
        self.distance = distance
        
def MeasureDistance(XYGridList):
    ser = serial.Serial('COM4')
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

XYGridList = []
XYGridList.append(XYGrid(0, 0, 2, 0.00))
XYGridList.append(XYGrid(1, 1, 2, 0.00))
XYGridList.append(XYGrid(2, 2, 2, 0.00)) 
XYGridList.append(XYGrid(3, 0, 1, 0.00))
XYGridList.append(XYGrid(4, 1, 1, 0.00))
XYGridList.append(XYGrid(5, 2, 1, 0.00))
XYGridList.append(XYGrid(6, 0, 0, 0.00))
XYGridList.append(XYGrid(7, 1, 0, 0.00))
XYGridList.append(XYGrid(8, 2, 0, 0.00))  

MeasureDistance(XYGridList)

averagePercentageFullSum = 0

for XYGrid in XYGridList:
    shelfHeight = 22
    sensorMeasurement = XYGrid.distance
    percentageFull = ((shelfHeight - sensorMeasurement) /shelfHeight) * 100
    print("idpos=",XYGrid.idpos,"xpos=",XYGrid.xpos,"ypos=",XYGrid.ypos,"distance=",XYGrid.distance, "percentageFull",percentageFull)
    
    averagePercentageFullSum = averagePercentageFullSum + percentageFull
    
averagePercentageFull = averagePercentageFullSum /9
print("Shelf is", averagePercentageFull,"% full")
    
stockLevel = checkStock(XYGrid, XYGridList)
print(stockLevel)

