def USFullness(shelfHeight, measurementCM):
    if measurementCM > shelfHeight:
        PercFull = 0
    if measurementCM < 0:
        PercFull = 1
    else:
        PercFull = (shelfHeight - measurementCM - 4) / shelfHeight
        
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
    
def CalculateEmptyBoxes(shelfHeight, measurementCM, lumens):
    b = PRFullness(lumens)   
    PercFull = (shelfHeight - measurementCM) / shelfHeight
    print ("Percfull is", PercFull, " b is ", b, "measurement is", measurementCM)
    if PercFull<= 0.1 and (b == 1 or b ==2):
        return 1
    else:
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
    singleshelf.priorityscore = GetProductPriorty(singleshelf, ProductList) * singleshelf.unitsOfSpace
    
def ShelfAvgVolumePercentFull (shelfLocation, shelfHeight, XYGridList):
    averagePercentageFullSum = 0 
    for XYGrid in XYGridList:
        if (XYGrid.shelflocation == shelfLocation):
            sensorMeasurement = XYGrid.USdistance
            if sensorMeasurement > shelfHeight + 4:
                sensorMeasurement = shelfHeight + 4
            percentageFull = 1 - ( (sensorMeasurement - 4) /shelfHeight)
            averagePercentageFullSum = averagePercentageFullSum + percentageFull
    averagePercentageFull =round((averagePercentageFullSum /9),2)
    if averagePercentageFull < 0:
        averagePercentageFull = 0
    if averagePercentageFull > 1:
        averagePercentageFull = 1
    return averagePercentageFull

def ShelfAvailableVolume (singleShelf):
    shelfVolume = singleShelf.height * singleShelf.width * singleShelf.depth
    OccupiedVolume = singleShelf.volumePercentFull * shelfVolume
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
    
#     db = sqlite3.connect(CreateDB.dbName)
#     cursor = db.cursor()
#             
#     cursor.execute('''SELECT id, shelfLocation, TPNB, unitsOfStock, percentageFull, timestamp FROM shelfGridTable''')
#     all_rows = cursor.fetchall()
#     count = 0
#     a = []
#     for row in all_rows:
#         if count > (cursor.rowcount-7):
#             print('{0} : {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2], row[3], row[4]))
#             test = ('{0}, {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2], row[3], row[4]))
#             test2 = test.split(',')
#             a.append(test2)
#         count = count + 1
#    print ("a-",a)      

    newlist = sorted(ShelfList, key=lambda x: (-x.priorityscore, -x.unitsOfSpace))
    master_list = []
    for singleshelf in newlist:
        master_list.append([singleshelf.tpnb, singleshelf.location, singleshelf.unitsOfSpace, singleshelf.imglocation, singleshelf.salesimglocation, singleshelf.confidenceLevel, singleshelf.priorityscore])
    return master_list