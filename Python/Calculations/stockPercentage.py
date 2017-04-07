import json
from Main.JordanAsad import shelfHeight

class StockPercentage:
    percentage = 0
    ifFull = "Looking Good!"
    ifEmpty = "Fill me UP!"
    count =0

def USFullness(shelfHeight, measurementCM):
    if measurementCM > shelfHeight:
        PercFull = 0
    else:
        PercFull = (shelfHeight - measurementCM) / shelfHeight
        
    #print("mes=",measurementCM, "%full=",PercFull)
        
    if (PercFull < 1/3):
        return 0
    elif (PercFull < 2/3 and PercFull > 1/3):
        return 1
    else:
        return 2

    
def PRFullness(lumens):
    if (lumens > 450):
        return 0
    elif (lumens > 100 and lumens < 450):
        return 1
    else:
        return 2
        
def CalculateConfidence(shelfHeight, measurementCM, lumens):
    a = USFullness(shelfHeight, measurementCM)
    b = PRFullness(lumens)
    if a == b:
        return a
    else:
        return -1
    
def UnitsToFill(singleshelf, ProductList, XYGridList,):
    for product in ProductList:
        if product.tpnb == singleshelf.tpnb:
            productVolume = product.height * product.width * product.depth
    
    shelfHeight = singleshelf.height
    shelfLocation = singleshelf.location
    # Work out percentage of volume filled
    singleshelf.volumePercentFull = ShelfAvgVolumePercentFull(shelfLocation, shelfHeight, XYGridList)
    # Convert to available space in cm^3
    availablevolume = ShelfAvailableVolume (singleshelf)
    occupiedVolume = ShelfOccupiedVolume(singleshelf)
    # Calculate number of units to fill the space
    
    unitsOccupied = int (occupiedVolume / productVolume)
    if unitsOccupied < 0:
        singleshelf.unitsOccupied = 0
    else:
        singleshelf.unitsOccupied = unitsOccupied
        
    unitsOfSpace = int(availablevolume / productVolume)
    if unitsOfSpace < 0:
        singleshelf.unitsOfSpace = 0
    else:
        singleshelf.unitsOfSpace = unitsOfSpace
    
def ShelfAvgVolumePercentFull (shelfLocation, shelfHeight, XYGridList):
    averagePercentageFullSum = 0 
    for XYGrid in XYGridList:
        if (XYGrid.shelflocation == shelfLocation):
            sensorMeasurement = XYGrid.USdistance
            percentageFull = 1 - ( (sensorMeasurement - 4) /shelfHeight)  
            averagePercentageFullSum = averagePercentageFullSum + percentageFull
    print("avg%fullsum=", averagePercentageFullSum)
    averagePercentageFull =round((averagePercentageFullSum /9),2)
    print(averagePercentageFull, "= abg percent full")
    if averagePercentageFull < 0.005 and averagePercentageFull > -0.05:
        averagePercentageFull = 0
    return averagePercentageFull

def ShelfAvailableVolume (singleShelf):
    shelfVolume = singleShelf.height * singleShelf.width * singleShelf.depth
    OccupiedVolume = singleShelf.volumePercentFull * shelfVolume
    print(singleShelf.location, "volume = ", shelfVolume, "volpercenfull=", singleShelf.volumePercentFull, "occupiedvolume=", OccupiedVolume)
    AvailableVolume = shelfVolume - OccupiedVolume
    return AvailableVolume

def ShelfOccupiedVolume (singleShelf):
    shelfVolume = singleShelf.height * singleShelf.width * singleShelf.depth
    OccupiedVolume = singleShelf.volumePercentFull * shelfVolume
    return OccupiedVolume

def GetProductPriorty(singleshelf, ProductList):
    for product in ProductList:
        if product.tpnb == singleshelf.tpnb:
            return product.priority
    return 0
    

def calculateFillListOrder(ShelfList, ProductList):
    for shelf in ShelfList:
        shelf.priorityscore = GetProductPriorty(shelf, ProductList) * shelf.unitsOfSpace
    
    #newlist = sorted(ShelfList, key=lambda x: (x.unitsOfSpace, reverse=True, ))
    newlist = sorted(ShelfList, key=lambda x: (-x.priorityscore, -x.unitsOfSpace))
    print("orig=", ShelfList)
    print("ordered=", newlist)
    
    master_list = []
    for singleshelf in newlist:
        print("shelf=",singleshelf.location,"%full=",singleshelf.volumePercentFull,"score",singleshelf.priorityscore)
        master_list.append([singleshelf.tpnb, singleshelf.location, singleshelf.unitsOfSpace, singleshelf.imglocation, singleshelf.salesimglocation, singleshelf.confidenceLevel, singleshelf.priorityscore])
    return master_list