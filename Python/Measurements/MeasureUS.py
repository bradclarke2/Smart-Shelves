import serial
import time

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