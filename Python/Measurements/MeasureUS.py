import serial
import time
import random
import Calculations.stockPercentage as stockpercentages

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
                #print("striping...")
                line = line.strip( 'US:' )
                line = line.strip("\r\n")
                listData = line.split(",")    
                #print("line=",listData)
                listData = [float(i) for i in listData]
                waiter = 0  
              
        for XYGrid in XYGridList:
            if ( XYGrid.shelflocation == singleshelf.location):
                XYGrid.USdistance = listData[XYGrid.idpos]
                #print("id=",XYGrid.idpos,"dist=",XYGrid.USdistance)
        
    else:   
        fullness = random.randint(0,2)
        
        if singleshelf.location == "6L1D":
            fullness = 3
        if singleshelf.location == "7L2B":
            fullness = 4
        
        
        for XYGrid in XYGridList:
            
            if fullness == 0:
                range_min = 0.0
                range_max = 18.0
            if fullness == 1:
                range_min = 13.0
                range_max = 32.0
            if fullness == 2:
                range_min = 28.0
                range_max = 55.0
                
            if fullness == 3:
                range_min = 0.0
                range_max = 14.0
                
            if fullness == 4:
                range_min = 31.0
                range_max = 45.0
                   
            if ( XYGrid.shelflocation == singleshelf.location):
                rand = random.uniform(range_min, range_max)
                print("rand=",rand,"res=",stockpercentages.USFullness(45, rand))
                XYGrid.USdistance = rand
             
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
