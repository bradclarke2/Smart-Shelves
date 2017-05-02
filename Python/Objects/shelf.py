class Shelf(object):
    def __init__(self,location, height,width, depth, tpnb):
        self.location = location
        self.height = height
        self.width = width
        self.depth = depth
        self.confidenceLevel = float(0.00) 
        self.areaFull = 0
        self.tpnb = tpnb
        self.unitsOccupied = 0
        self.unitsOfSpace = 0
        self.imglocation = ""
        self.salesimglocation = ""
        self.volumePercentFull = 0
        self.USpointscovered = 0
        self.PRpointscovered = 0
        self.priorityscore = 0   

def makeShelfGrid(): 
    MadeList = []
#    MadeList.append(Shelf("1L4B", 41, 50.0, 20.0, "5053827141529"))
    MadeList.append(Shelf("2R6A", 41, 50.0, 20.0, "5051140150471"))
    MadeList.append(Shelf("3L5A", 41, 50.0, 20.0, "5010003000131"))
    MadeList.append(Shelf("4L1B", 41, 50.0, 20.0, "5053526716035"))
    MadeList.append(Shelf("4R4B", 41, 50.0, 20.0, "0000010001875"))
    MadeList.append(Shelf("5L2C", 41, 50.0, 20.0, "5053947211041"))
    MadeList.append(Shelf("6L1D", 41, 50.0, 20.0, "5000462416734"))
    MadeList.append(Shelf("7L2B", 41, 50.0, 20.0, "5010024101381"))
    MadeList.append(Shelf("8L2B", 41, 50.0, 20.0, "5012035936631"))
    MadeList.append(Shelf("9L2B", 41, 50.0, 20.0, "5010204427379"))
    MadeList.append(Shelf("10L2B", 41, 50.0, 20.0, "5000209114510"))
    MadeList.append(Shelf("11L2B", 41, 50.0, 20.0, "5000436725589"))
    return MadeList