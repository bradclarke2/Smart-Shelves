class Shelf(object):
    def __init__(self,location, height,width, depth, tpnb):
        self.location = location
        self.height = height
        self.width = width
        self.depth = depth
        self.volumePercentFull = 0
        self.areaFull = 0
        self.tpnb = tpnb
        self.unitsOccupied = 0
        self.unitsOfSpace = 0
        self.imglocation = ""
        self.salesimglocation = ""    

def makeShelfGrid(): 
    MadeList = []
    MadeList.append(Shelf("1L4B", 47, 50.0, 20.0, "06260901"))
    MadeList.append(Shelf("2R6A", 22.54, 50.0, 20.0, "050060302"))
    MadeList.append(Shelf("3L5A", 22.54, 50.0, 20.0, "062609003"))
    MadeList.append(Shelf("4L1B", 22.54, 50.0, 20.0, "062609003"))
    MadeList.append(Shelf("4R4B", 22.54, 50.0, 20.0, "062609005"))
    MadeList.append(Shelf("5L2C", 22.54, 50.0, 20.0, "050060306"))
    MadeList.append(Shelf("6L1D", 22.54, 50.0, 20.0, "062609007"))
    MadeList.append(Shelf("7L2B", 22.54, 50.0, 20.0, "050060308"))
    return MadeList