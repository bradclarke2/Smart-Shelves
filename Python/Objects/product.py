class Product (object): 
    def __init__(self,name, tpnb, height, width, depth, weight):
        self.name = name
        self.tpnb = tpnb
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight

def makeProductGrid(): 
    MadeList = []
    MadeList.append(Product("Quaker Oats", "062609056", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Kellogs Cornflakes", "050060399", 30, 23, 8, 0.450))
    return MadeList