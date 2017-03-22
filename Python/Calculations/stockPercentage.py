from Main.JordanAsad import shelfHeight
class StockPercentage:
    percentage = 0
    ifFull = "Looking Good!"
    ifEmpty = "Fill me UP!"
    count =0

def checkStock(XYGrid, XYGridList):
    count = 0
    for XYGrid in XYGridList:
        if XYGrid.distance < 20:
            count = count +1
    percentage = (count/XYGridList.__len__())
    return percentage

def SingleEmptyFull(shelfHeight, measurementCM):
    PercFull = measurementCM / shelfHeight
    if (PercFull < 1/3):
        return 0
    elif (PercFull < 2/3 and PercFull > 1/3):
        return 1
    elif (PercFull > 2/3):
        return 2   
    
    
 
def ShelfAvgPercentageFull (shelfHeight, XYGridList):
    averagePercentageFullSum =0 
    for XYGrid in XYGridList:

        sensorMeasurement = XYGrid.distance
        percentageFull = ((shelfHeight - sensorMeasurement) /shelfHeight)
        print("idpos=",XYGrid.idpos,"xpos=",XYGrid.xpos,"ypos=",XYGrid.ypos,"distance=",XYGrid.distance, "percentageFull",percentageFull)
         
        averagePercentageFullSum = averagePercentageFullSum + percentageFull
         
    averagePercentageFull =round((averagePercentageFullSum /9),2)
    print("Volume = ", averagePercentageFull * 100, " % full")
         
    stockLevel = checkStock(XYGrid, XYGridList)
    print("Surface Area = ", round(stockLevel,2) * 100, " % full")
    return averagePercentageFull
    