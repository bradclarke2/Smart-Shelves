import Sensor

class Shelf (object):
    height = 0
    width = 0
    depth = 0
    location = ""
    sensor = Sensor

    def __init__(self,height,width, depth, location):
        self.height = height
        self.width = width
        self.depth = depth
        self.location = location

def makeShelf(height, width, depth, location): 
    shelf = Shelf(height, width, depth, location)
    return shelf