class Shelf(object):
    def __init__(self,location, height,width, depth):
        self.location = location
        self.height = height
        self.width = width
        self.depth = depth

def makeShelfGrid(): 
    MadeList = []
    MadeList.append(Shelf("14L8E", 30.0, 50.0, 20.0))
    MadeList.append(Shelf("15R2A", 40.0, 50.0, 1.0))
    return MadeList