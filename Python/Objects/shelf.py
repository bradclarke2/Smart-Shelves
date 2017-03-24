class Shelf(object):
    def __init__(self,location, height,width, depth, tpnb):
        self.location = location
        self.height = height
        self.width = width
        self.depth = depth
        self.volumePercentFull = 0
        self.areaFull = 0
        self.tpnb = tpnb
        self.unitsOfSpace = 0

def makeShelfGrid(): 
    MadeList = []
    MadeList.append(Shelf("14L8E", 30.0, 50.0, 20.0, "062609056"))
    MadeList.append(Shelf("15R2A", 30.0, 50.0, 20.0, "050060399"))
    return MadeList