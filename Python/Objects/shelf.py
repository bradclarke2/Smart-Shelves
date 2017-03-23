import Sensor

class Shelf (object):
    def __init__(self,height,width, depth, location):
        self.height = 0
        self.width = 0
        self.depth = 0
        self.location = ""
        self.sensor = Sensor

def makeShelf(height, width, depth, location): 
    shelf = Shelf(height, width, depth, location)
    return shelf