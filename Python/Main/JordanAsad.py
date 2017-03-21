class StockPercentageVolume:
    percentage=0
    count =0

def checkStock(XYGrid, XYGridList):
    count = 0
    for XYGrid in XYGridList:
        if XYGrid.distance < 20:
            count = count +1
    percentage = (count/XYGridList.__len__())*100
    return percentage

shelfHeight = 100
sensorMeasurement = 20

percentageFull = ((shelfHeight - sensorMeasurement) /shelfHeight) * 100

print(percentageFull)
