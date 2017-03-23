import Calculations.stockPercentage as stockpercentages
import Graphing.Heatmap as heatmap
import Measurements.MeasureUS as measureUS
import WebPage.API as startAPI
import Objects.XYGrid as XYGridObject

class ShelfLocationGrid(object):
    """__init__() functions as the class constructor"""
    def __init__(self, shelflocation = None, idpos=None, xpos = None, ypos = None, distance = None):
        self.shelflocation = shelflocation
        self.percentagefull = distance
        
ShelfLocations = ["14L8E" , "15R2A"]

XYGridList = XYGridObject.MakeXYGrid()
print(XYGridList)
    
for singleshelfpos in ShelfLocations:
    measureUS.MeasureDistance(singleshelfpos, XYGridList)    
    stockpercentages.UnitsToFill(singleshelfpos, XYGridList)
    heatmap.MakeHeatMap(stockpercentages.shelfHeight, XYGridList, singleshelfpos)
    
startAPI.startfunction()