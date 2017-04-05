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
    MadeList.append(Product("Quaker Oats", "5000108810988", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Pancake Mix", "0000003265314", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Cat Food", "8410136002885", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Water 500ml", "5060108450324", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Caviar", "5701263907864", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Dino Prosecco", "5053947211041", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Stawberry Jam", "5000119002501", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Peanuts 200g", "5052109944841", 21.0, 13.0, 8.0, 0.293))
    #MadeList.append(Product("Kellogs Cornflakes", "050060399", 30, 23, 8, 0.450))
    return MadeList