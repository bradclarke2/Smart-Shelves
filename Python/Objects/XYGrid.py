class XYGrid(object):
    """__init__() functions as the class constructor"""
    def __init__(self, shelflocation = None, idpos=None, xpos = None, ypos = None):
        self.shelflocation = shelflocation
        self.idpos = idpos
        self.xpos = xpos
        self.ypos = ypos
        self.USdistance = float(0.00)
        self.PRCovered = 0
                
def MakeXYGrid():
    MadeList = []
    MadeList.append(XYGrid("1L4B", 0, 0, 0))
    MadeList.append(XYGrid("1L4B", 1, 0, 1))
    MadeList.append(XYGrid("1L4B", 2, 0, 2)) 
    MadeList.append(XYGrid("1L4B", 3, 1, 0))
    MadeList.append(XYGrid("1L4B", 4, 1, 1))
    MadeList.append(XYGrid("1L4B", 5, 1, 2))
    MadeList.append(XYGrid("1L4B", 6, 2, 0))
    MadeList.append(XYGrid("1L4B", 7, 2, 1))
    MadeList.append(XYGrid("1L4B", 8, 2, 2))
     
    MadeList.append(XYGrid("2R6A", 9, 0, 0))
    MadeList.append(XYGrid("2R6A", 10, 0, 1))
    MadeList.append(XYGrid("2R6A", 11, 0, 2)) 
    MadeList.append(XYGrid("2R6A", 12, 1, 0))
    MadeList.append(XYGrid("2R6A", 13, 1, 1))
    MadeList.append(XYGrid("2R6A", 14, 1, 2))
    MadeList.append(XYGrid("2R6A", 15, 2, 0))
    MadeList.append(XYGrid("2R6A", 16, 2, 1))
    MadeList.append(XYGrid("2R6A", 17, 2, 2))
     
    MadeList.append(XYGrid("3L5A", 999, 0, 0))
    MadeList.append(XYGrid("3L5A", 9910, 0, 1))
    MadeList.append(XYGrid("3L5A", 9911, 0, 2)) 
    MadeList.append(XYGrid("3L5A", 9912, 1, 0))
    MadeList.append(XYGrid("3L5A", 9913, 1, 1))
    MadeList.append(XYGrid("3L5A", 9914, 1, 2))
    MadeList.append(XYGrid("3L5A", 9915, 2, 0))
    MadeList.append(XYGrid("3L5A", 9916, 2, 1))
    MadeList.append(XYGrid("3L5A", 9917, 2, 2))
     
    MadeList.append(XYGrid("4L1B", 999, 0, 0))
    MadeList.append(XYGrid("4L1B", 9910, 0, 1))
    MadeList.append(XYGrid("4L1B", 9911, 0, 2)) 
    MadeList.append(XYGrid("4L1B", 9912, 1, 0))
    MadeList.append(XYGrid("4L1B", 9913, 1, 1))
    MadeList.append(XYGrid("4L1B", 9914, 1, 2))
    MadeList.append(XYGrid("4L1B", 9915, 2, 0))
    MadeList.append(XYGrid("4L1B", 9916, 2, 1))
    MadeList.append(XYGrid("4L1B", 9917, 2, 2))
     
    MadeList.append(XYGrid("4R4B", 999, 0, 0))
    MadeList.append(XYGrid("4R4B", 9910, 0, 1))
    MadeList.append(XYGrid("4R4B", 9911, 0, 2)) 
    MadeList.append(XYGrid("4R4B", 9912, 1, 0))
    MadeList.append(XYGrid("4R4B", 9913, 1, 1))
    MadeList.append(XYGrid("4R4B", 9914, 1, 2))
    MadeList.append(XYGrid("4R4B", 9915, 2, 0))
    MadeList.append(XYGrid("4R4B", 9916, 2, 1))
    MadeList.append(XYGrid("4R4B", 9917, 2, 2))
     
    MadeList.append(XYGrid("5L2C", 999, 0, 0))
    MadeList.append(XYGrid("5L2C", 9910, 0, 1))
    MadeList.append(XYGrid("5L2C", 9911, 0, 2)) 
    MadeList.append(XYGrid("5L2C", 9912, 1, 0))
    MadeList.append(XYGrid("5L2C", 9913, 1, 1))
    MadeList.append(XYGrid("5L2C", 9914, 1, 2))
    MadeList.append(XYGrid("5L2C", 9915, 2, 0))
    MadeList.append(XYGrid("5L2C", 9916, 2, 1))
    MadeList.append(XYGrid("5L2C", 9917, 2, 2))
     
    MadeList.append(XYGrid("6L1D", 999, 0, 0))
    MadeList.append(XYGrid("6L1D", 9910, 0, 1))
    MadeList.append(XYGrid("6L1D", 9911, 0, 2)) 
    MadeList.append(XYGrid("6L1D", 9912, 1, 0))
    MadeList.append(XYGrid("6L1D", 9913, 1, 1))
    MadeList.append(XYGrid("6L1D", 9914, 1, 2))
    MadeList.append(XYGrid("6L1D", 9915, 2, 0))
    MadeList.append(XYGrid("6L1D", 9916, 2, 1))
    MadeList.append(XYGrid("6L1D", 9917, 2, 2))
     
    MadeList.append(XYGrid("7L2B", 999, 0, 0))
    MadeList.append(XYGrid("7L2B", 9910, 0, 1))
    MadeList.append(XYGrid("7L2B", 9911, 0, 2)) 
    MadeList.append(XYGrid("7L2B", 9912, 1, 0))
    MadeList.append(XYGrid("7L2B", 9913, 1, 1))
    MadeList.append(XYGrid("7L2B", 9914, 1, 2))
    MadeList.append(XYGrid("7L2B", 9915, 2, 0))
    MadeList.append(XYGrid("7L2B", 9916, 2, 1))
    MadeList.append(XYGrid("7L2B", 9917, 2, 2))
    return MadeList
