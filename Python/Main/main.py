import Calculations.stockPercentage as stockpercentages
import Measurements.MeasureUS as measureUS
        
class XYGrid(object):
    """__init__() functions as the class constructor"""
    def __init__(self, idpos=None, xpos = None, ypos = None, distance = None):
        self.idpos = idpos
        self.xpos = xpos
        self.ypos = ypos
        self.distance = distance

#checkStock.checkStock(XYGrid, XYGridList)

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
        GridTemp=[]
        for XYGrid in XYGridList:
            GridTemp.append([XYGrid.idpos, XYGrid.xpos, XYGrid.ypos, XYGrid.distance])
        return GridTemp            
 
api.add_resource(Departmental_Salary, '/measurements/')

app.run()