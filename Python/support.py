global sensorNumbers

ifFull = "Looking Good!"
ifEmpty = "Fill me UP!"

def checkStock(sensorDistance):
    for b in range(0,sensorNumbers):
        if sensorDistance [b] < 20:
            fullStatus [b] = ifFull
        else:
            fullStatus [b] = ifEmpty
    print(fullStatus)

numberOfItems = 0
shelfPercentage = 0

#def checkShelfPercentage(sensorDistance):
#    global numberOfItems
#    numberOfItems = 0
#    for c in range(0,sensorNumbers):
#        if fullStatus [c] == ifFull:
#            numberOfItems = numberOfItems + 1
#    shelfPercentage = (numberOfItems/sensorNumbers)*100
#    print(shelfPercentage)
#    return shelfPercentage