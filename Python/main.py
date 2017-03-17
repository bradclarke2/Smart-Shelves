import serial
import time

class USSensor(object):
    """__init__() functions as the class constructor"""
    def __init__(self, name=None, xypos = None, trig_pin = None, echo_pin = None):
        self.name = name
        self.xypos = xypos
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        
class XYGrid(object):
    """__init__() functions as the class constructor"""
    def __init__(self, name=None, trig_pin = None, echo_pin = None, distance = None):
        self.name = name
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.distance = distance
        
def MeasureDistance(USSensor): 
    ser = serial.Serial('COM9')
    time.sleep(5)
    
    while True:
        line = str(ser.readline(),'utf-8')
        line = line.strip("\r\n")
        listData = line.split(",")    
        print("line=",listData)

#make a list of class USSensor(s)
XYGridList = []
XYGridList.append(XYGrid("0",0, 0,0.00))
XYGridList.append(XYGrid("1",0, 1,0.00))
XYGridList.append(XYGrid("2",0, 2,0.00))

USSensorList = []
USSensorList.append(USSensor("Sensor1",0, 53, 52))
USSensorList.append(USSensor("Sensor2",1, 51, 50))
USSensorList.append(USSensor("Sensor3",2, 49, 48))

for XYGrid in XYGridList:
    for USSensor in USSensorList:
        if int(USSensor.xypos) == int(XYGrid.name):
            print("match,xypos=",USSensor.xypos,"name=",XYGrid.name)
            XYGrid.distance = MeasureDistance(USSensor)
            print("xygriddist=",XYGrid.distance)
        else:
            print("nomatch,xypos=",USSensor.xypos,"name=",XYGrid.name)