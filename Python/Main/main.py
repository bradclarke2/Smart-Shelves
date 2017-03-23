import Calculations.stockPercentage as stockpercentages
import Measurements.MeasureUS as measureUS
import WebPage.API as startAPI
        
class XYGrid(object):
    """__init__() functions as the class constructor"""
    def __init__(self, shelflocation = None, idpos=None, xpos = None, ypos = None, distance = None):
        self.shelflocation = shelflocation
        self.idpos = idpos
        self.xpos = xpos
        self.ypos = ypos
        self.distance = distance
        
class ShelfLocationGrid(object):
    """__init__() functions as the class constructor"""
    def __init__(self, shelflocation = None, idpos=None, xpos = None, ypos = None, distance = None):
        self.shelflocation = shelflocation
        self.percentagefull = distance
        
ShelfLocations = ["14L8E" , "15R2A"]

#checkStock.checkStock(XYGrid, XYGridList)

XYGridList = []
<<<<<<< HEAD
XYGridList.append(XYGrid(0, 0, 0, 0.00))
XYGridList.append(XYGrid(1, 0, 1, 0.00))
XYGridList.append(XYGrid(2, 0, 2, 0.00)) 
XYGridList.append(XYGrid(3, 1, 0, 0.00))
XYGridList.append(XYGrid(4, 1, 1, 0.00))
XYGridList.append(XYGrid(5, 1, 2, 0.00))
XYGridList.append(XYGrid(6, 2, 0, 0.00))
XYGridList.append(XYGrid(7, 2, 1, 0.00))
XYGridList.append(XYGrid(8, 2, 2, 0.00))  

measureUS.MeasureDistance(XYGridList)

shelfHeight = 30
percentageVolumeOccupied = stockpercentages.ShelfAvgPercentageFull(shelfHeight, XYGridList)

shelfVolume = 21*40*17
productVolume = 21*12.5*8
occupiedVolume = percentageVolumeOccupied * shelfVolume

volumeOfFreeSpace = shelfVolume - occupiedVolume

print(int(volumeOfFreeSpace / productVolume), "This is how many Quaker Oats can go out")

#heatmap.MakeHeatMap(shelfHeight, XYGridList, "14L16E")

percentageVolumeOccupied = stockpercentages.ShelfAvgPercentageFull(shelfHeight, XYGridList)

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Departmental_Salary(Resource):
    def get(self):          
        return percentageVolumeOccupied



class Shelf_Location(Resource):
    def get(self):
        XYGridList = []
        XYGridList.append(XYGrid(0, 0, 0, 0.00))
        XYGridList.append(XYGrid(1, 0, 1, 0.00))
        XYGridList.append(XYGrid(2, 0, 2, 0.00)) 
        XYGridList.append(XYGrid(3, 1, 0, 0.00))
        XYGridList.append(XYGrid(4, 1, 1, 0.00))
        XYGridList.append(XYGrid(5, 1, 2, 0.00))
        XYGridList.append(XYGrid(6, 2, 0, 0.00))
        XYGridList.append(XYGrid(7, 2, 1, 0.00))
        XYGridList.append(XYGrid(8, 2, 2, 0.00))  
        measureUS.MeasureDistance(XYGridList)
        shelfLocation = stockpercentages.ShelfAvgPercentageFull(shelfHeight, XYGridList)
        print(shelfLocation)
        return shelfLocation   
     
api.add_resource(Shelf_Location, '/shelflocation/')
api.add_resource(Departmental_Salary, '/measurements/')

app.run()
=======
XYGridList.append(XYGrid("14L8E", 0, 0, 0, 0.00))
XYGridList.append(XYGrid("14L8E", 1, 0, 1, 0.00))
XYGridList.append(XYGrid("14L8E", 2, 0, 2, 0.00)) 
XYGridList.append(XYGrid("14L8E", 3, 1, 0, 0.00))
XYGridList.append(XYGrid("14L8E", 4, 1, 1, 0.00))
XYGridList.append(XYGrid("14L8E", 5, 1, 2, 0.00))
XYGridList.append(XYGrid("14L8E", 6, 2, 0, 0.00))
XYGridList.append(XYGrid("14L8E", 7, 2, 1, 0.00))
XYGridList.append(XYGrid("14L8E", 8, 2, 2, 0.00)) 
XYGridList.append(XYGrid("15R2A", 9, 0, 0, 0.00))
XYGridList.append(XYGrid("15R2A", 10, 0, 1, 0.00))
XYGridList.append(XYGrid("15R2A", 11, 0, 2, 0.00)) 
XYGridList.append(XYGrid("15R2A", 12, 1, 0, 0.00))
XYGridList.append(XYGrid("15R2A", 13, 1, 1, 0.00))
XYGridList.append(XYGrid("15R2A", 14, 1, 2, 0.00))
XYGridList.append(XYGrid("15R2A", 15, 2, 0, 0.00))
XYGridList.append(XYGrid("15R2A", 16, 2, 1, 0.00))
XYGridList.append(XYGrid("15R2A", 17, 2, 2, 0.00))   
    
for singleshelfpos in ShelfLocations:
    measureUS.MeasureDistance(singleshelfpos, XYGridList)    
    stockpercentages.UnitsToFill(singleshelfpos, XYGridList)
    heatmap.MakeHeatMap(stockpercentages.shelfHeight, XYGridList, singleshelfpos)
    
startAPI.startfunction()
>>>>>>> 59b0ca3c1724944a05fec4d88a2d1e63fb5efcb7
