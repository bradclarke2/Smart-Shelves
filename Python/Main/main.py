import serial
import time
from Calculations import support
        
class XYGrid(object):
    """__init__() functions as the class constructor"""

    def __init__(self, idpos=None, xpos = None, ypos = None, distance = None):
        self.idpos = idpos
        self.xpos = xpos
        self.ypos = ypos
        self.distance = distance
        
def MeasureDistance(XYGridList):
    ser = serial.Serial('COM9')
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
XYGridList.append(XYGrid(0, 6, 7,0.00))
XYGridList.append(XYGrid(1, 6, 7,0.00))
XYGridList.append(XYGrid(2, 6, 7,0.00)) 

MeasureDistance(XYGridList)

for XYGrid in XYGridList:
    print("idpos=",XYGrid.idpos,"xpos=",XYGrid.xpos,"ypos=",XYGrid.ypos,"distance=",XYGrid.distance)
    
support.checkStock(XYGrid)
