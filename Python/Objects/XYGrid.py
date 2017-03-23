class XYGrid(object):
    """__init__() functions as the class constructor"""
    def __init__(self, shelflocation = None, idpos=None, xpos = None, ypos = None, distance = None):
        self.shelflocation = shelflocation
        self.idpos = idpos
        self.xpos = xpos
        self.ypos = ypos
        self.distance = distance
        
def MakeXYGrid():
    MadeList = []
    MadeList.append(XYGrid("14L8E", 0, 0, 0, 0.00))
    MadeList.append(XYGrid("14L8E", 1, 0, 1, 0.00))
    MadeList.append(XYGrid("14L8E", 2, 0, 2, 0.00)) 
    MadeList.append(XYGrid("14L8E", 3, 1, 0, 0.00))
    MadeList.append(XYGrid("14L8E", 4, 1, 1, 0.00))
    MadeList.append(XYGrid("14L8E", 5, 1, 2, 0.00))
    MadeList.append(XYGrid("14L8E", 6, 2, 0, 0.00))
    MadeList.append(XYGrid("14L8E", 7, 2, 1, 0.00))
    MadeList.append(XYGrid("14L8E", 8, 2, 2, 0.00)) 
    MadeList.append(XYGrid("15R2A", 9, 0, 0, 0.00))
    MadeList.append(XYGrid("15R2A", 10, 0, 1, 0.00))
    MadeList.append(XYGrid("15R2A", 11, 0, 2, 0.00)) 
    MadeList.append(XYGrid("15R2A", 12, 1, 0, 0.00))
    MadeList.append(XYGrid("15R2A", 13, 1, 1, 0.00))
    MadeList.append(XYGrid("15R2A", 14, 1, 2, 0.00))
    MadeList.append(XYGrid("15R2A", 15, 2, 0, 0.00))
    MadeList.append(XYGrid("15R2A", 16, 2, 1, 0.00))
    MadeList.append(XYGrid("15R2A", 17, 2, 2, 0.00))
    return MadeList
