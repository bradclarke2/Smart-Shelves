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
    MadeList.append(Product("Quaker Oats", "06260901", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Pancake Mix", "050060302", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Cat Food", "062609003", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Water 500ml", "050060304", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Caviar", "062609005", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Dino Prosecco", "050060306", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Stawberry Jam", "062609007", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Peanuts 200g", "050060308", 21.0, 13.0, 8.0, 0.293))
    #MadeList.append(Product("Kellogs Cornflakes", "050060399", 30, 23, 8, 0.450))
    return MadeList