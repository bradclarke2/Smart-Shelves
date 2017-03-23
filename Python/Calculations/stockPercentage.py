productVolume = 21*12.5*8

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
    
def UnitsToFill(singleshelf, XYGridList):
    shelfHeight = singleshelf.height
    shelfLocation = singleshelf.location
    print("height=", shelfHeight, "loc=", shelfLocation)
    # Work out percentage of volume filled
    singleshelf.volumePercentFull = ShelfAvgVolumePercentFull(shelfLocation, shelfHeight, XYGridList)
    # Convert to available space in cm^3
    availablevolume = ShelfOccupiedVolume (singleshelf)
    # Calculate number of units to fill the space
    singleshelf.unitsOfSpace = int(availablevolume / productVolume) 

        
 
def ShelfAvgVolumePercentFull (shelfLocation, shelfHeight, XYGridList):
    averagePercentageFullSum = 0 
    for XYGrid in XYGridList:
        if (XYGrid.shelflocation == shelfLocation):
            sensorMeasurement = XYGrid.distance
            percentageFull = ((shelfHeight - sensorMeasurement) /shelfHeight)  
            averagePercentageFullSum = averagePercentageFullSum + percentageFull
    print("avg%fullsum=", averagePercentageFullSum)
    averagePercentageFull =round((averagePercentageFullSum /9),2)
    return averagePercentageFull

def ShelfOccupiedVolume (singleShelf):
    shelfVolume = singleShelf.height * singleShelf.width * singleShelf.depth
    
    OccupiedVolume = singleShelf.volumePercentFull * shelfVolume
    print(singleShelf.location, "volume = ", shelfVolume, "volpercenfull=", singleShelf.volumePercentFull, "occupiedvolume=", OccupiedVolume)
    AvailableVolume = shelfVolume - OccupiedVolume
    return AvailableVolume