import serial
import time
import random

def MeasureDistanceUS(singleshelf, XYGridList):
    
    if singleshelf.location == "1L4B":
        ser = serial.Serial('COM9', 9600)
        ser.readline()
        time.sleep(1)
         
        waiter = 1
         
        while waiter == 1:
            line = str(ser.readline(),'utf-8')
            line = line.strip("\r\n")
             
            print(line)
             
            if line.startswith("US:"):
                print("striping...")
                line = line.strip( 'US:' )
                line = line.strip("\r\n")
                listData = line.split(",")    
                print("line=",listData)
                listData = [float(i) for i in listData]
                waiter = 0  
              
        for XYGrid in XYGridList:
            if ( XYGrid.shelflocation == singleshelf.location):
                XYGrid.USdistance = listData[XYGrid.idpos]
                print("id=",XYGrid.idpos,"dist=",XYGrid.USdistance)
        
    else:   
        for XYGrid in XYGridList:
            if ( XYGrid.shelflocation == singleshelf.location):
                XYGrid.USdistance = random.random() * 24  
             
def MeasureDistancePR(singleshelf, XYGridList):
    
    if singleshelf.location == "1L4B":
        ser = serial.Serial('COM9', 9600)
        ser.readline()
        time.sleep(1)
         
        waiter = 1
         
        while waiter == 1:
            line = str(ser.readline(),'utf-8')
            line = line.strip("\r\n")
            
            print(line)
             
            if line.startswith("PR:"):
                print("striping...")
                line = line.strip( 'PR:' )
                line = line.strip("\r\n")
                listData = line.split(",")    
                print("line=",listData)
                listData = [float(i) for i in listData]
                waiter = 0  
              
        for XYGrid in XYGridList:
            if ( XYGrid.shelflocation == singleshelf.location):
                XYGrid.PRCovered = listData[XYGrid.idpos]
                print("id=",XYGrid.idpos,"dist=",XYGrid.PRCovered)
        
        
    else:
        for XYGrid in XYGridList:
            if ( XYGrid.shelflocation == singleshelf.location):
                XYGrid.PRCovered = random.random() * 1000  
