import serial
import time

class USSensor(object):
    """__init__() functions as the class constructor"""
    def __init__(self, idpos=None, xypos = None, trig_pin = None, echo_pin = None):
        self.idpos = idpos
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        
class XYGrid(object):
    """__init__() functions as the class constructor"""
    def __init__(self, idpos=None, xpos = None, ypos = None, distance = None):
        self.idpos = idpos
        self.xpos = xpos
        self.ypos = ypos
        self.distance = distance
        
def MeasureDistance(USidpos):
    #return 1.00
    print(USidpos)
    ser = serial.Serial('COM9')
    time.sleep(5)
    while True:
        line = str(ser.readline(),'utf-8')
        line = line.strip("\r\n")
        listData = line.split(",")    
        print("line=",listData)
        return listData[USidpos]

#make a list of class USSensor(s)
XYGridList = []
XYGridList.append(XYGrid(0, 6, 7,0.00))
XYGridList.append(XYGrid(1, 6, 7,0.00))
XYGridList.append(XYGrid(2, 6, 7,0.00)) 

USSensorList = []
USSensorList.append(USSensor(1, 6))
USSensorList.append(USSensor(5, 6))
USSensorList.append(USSensor(3, 6))

for XYGrid in XYGridList:
    for USSensor in USSensorList:
        if int(USSensor.idpos) == int(XYGrid.idpos):
            print("match,xypos=",USSensor.idpos,"name=",XYGrid.idpos)
            XYGrid.distance = MeasureDistance(USSensor.idpos)
            print("xygriddist=",XYGrid.distance)
        else:
            print("nomatch,xypos=",USSensor.idpos,"name=",XYGrid.idpos)