class Shelf(object):
    def __init__(self,location, height,width, depth):
        self.location = location
        self.height = height
        self.width = width
        self.depth = depth
        self.volumePercentFull = 0
        self.areaFull = 0
        self.unitsOfSpace = 0
        

def makeShelfGrid(): 
    MadeList = []
    MadeList.append(Shelf("14L8E", 30.0, 50.0, 20.0))
    MadeList.append(Shelf("15R2A", 30.0, 25.0, 20.0))
    return MadeList