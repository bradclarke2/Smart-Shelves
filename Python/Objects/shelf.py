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

def makeShelfGrid(): 
    MadeList = []

    MadeList.append(Shelf("1L4B", 45, 50.0, 20.0, "5000108810988"))
#    MadeList.append(Shelf("2R6A", 45, 50.0, 20.0, "0000003265314"))
#     MadeList.append(Shelf("3L5A", 22.54, 50.0, 20.0, "8410136002885"))
#     MadeList.append(Shelf("4L1B", 22.54, 50.0, 20.0, "5060108450324"))
#     MadeList.append(Shelf("4R4B", 22.54, 50.0, 20.0, "5701263907864"))
#     MadeList.append(Shelf("5L2C", 22.54, 50.0, 20.0, "5053947211041"))
#     MadeList.append(Shelf("6L1D", 22.54, 50.0, 20.0, "5000119002501"))
#     MadeList.append(Shelf("7L2B", 22.54, 50.0, 20.0, "5052109944841"))
    return MadeList