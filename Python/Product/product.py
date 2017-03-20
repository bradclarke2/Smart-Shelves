import Shelf

class Product (object):
    height = 0
    width = 0
    depth = 0
    weight = 0
    tpnb = ""
    shelf = Shelf
    
    def __init__(self,height,width, depth, weight, tpnb, shelf):
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight
        self.tpnb = tpnb
        self.shelf = shelf

def makeProduct(height, width, depth, weight, tpnb, shelf): 
    product = Product(height, width, depth, weight, tpnb, shelf)
    return product