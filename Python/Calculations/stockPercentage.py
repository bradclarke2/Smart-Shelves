from Main.main import XYGridList
global sensorNumbers

ifFull = "Looking Good!"
ifEmpty = "Fill me UP!"
count =0

def checkStock(XYGrid):
    count = 0
    for XYGrid in XYGridList:
        if XYGrid.distance < 20:
            count = count +1
    shelfPercentage = (count/XYGridList.__len__())*100
    return shelfPercentage

#def checkShelfPercentage(sensorDistance):
#    global numberOfItems
#    numberOfItems = 0
#    for c in range(0,sensorNumbers):
#        if fullStatus [c] == ifFull:
#            numberOfItems = numberOfItems + 1
#    shelfPercentage = (numberOfItems/sensorNumbers)*100
#    print(shelfPercentage)
#    return shelfPercentage