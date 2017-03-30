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
        

def makeShelfGrid(): 
    MadeList = []
    MadeList.append(Shelf("14L8E", 22.54, 100.0, 20.0, "062609056"))
    MadeList.append(Shelf("15R2A", 22.54, 500.0, 20.0, "050060399"))
    return MadeList