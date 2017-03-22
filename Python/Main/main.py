import Calculations.stockPercentage as stockpercentages
import Graphing.Heatmap as heatmap
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

shelfHeight = 30

measureUS.MeasureDistance(XYGridList)

for XYGrid in XYGridList:
    print(XYGrid.distance)

heatmap.MakeHeatMap(shelfHeight, XYGridList, "14L16E")

stockpercentages.ShelfAvgPercentageFull(shelfHeight, XYGridList)