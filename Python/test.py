import serial
import time

ser = serial.Serial('COM9')
time.sleep(2)
waiter = 1
print("waiter=",waiter)
while waiter == 1:
    line = str(ser.readline(),'utf-8')
    line = line.strip("\r\n")
    listData = line.split(",")    
    print("line=",listData)
    
    print(type(float(listData[0])))
    
    print("bool=",isinstance(listData[0], float))
    
    if ( isinstance(listData[0], float) ):
        for XYGrid in XYGridList:
            XYGrid.distance = listData[XYGrid.idpos]
        waiter = 0
        print("waiter=",waiter)         
