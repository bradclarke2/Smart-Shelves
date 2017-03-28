class StockPercentage:
    percentage = 0
    ifFull = "Looking Good!"
    ifEmpty = "Fill me UP!"
    count =0

def SingleEmptyFull(shelfHeight, measurementCM):
    PercFull = measurementCM / shelfHeight
    if (PercFull < 1/3):
        return 2
    elif (PercFull < 2/3 and PercFull > 1/3):
        return 1
    elif (PercFull > 2/3):
        return 0   
    
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
    singleshelf.unitsOccupied = int (occupiedVolume / productVolume)
    singleshelf.unitsOfSpace = int(availablevolume / productVolume)

def ShelfAvgVolumePercentFull (shelfLocation, shelfHeight, XYGridList):
    averagePercentageFullSum = 0 
    for XYGrid in XYGridList:
        if (XYGrid.shelflocation == shelfLocation):
            sensorMeasurement = XYGrid.distance
            percentageFull = 1 - ( (sensorMeasurement - 4) /shelfHeight)  
            averagePercentageFullSum = averagePercentageFullSum + percentageFull
    print("avg%fullsum=", averagePercentageFullSum)
    averagePercentageFull =round((averagePercentageFullSum /9),2)
    if averagePercentageFull < 0.001 and averagePercentageFull > -0.05:
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