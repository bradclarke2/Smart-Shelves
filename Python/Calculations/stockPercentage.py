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
    percentage = (count/XYGridList.__len__())*100
    return percentage