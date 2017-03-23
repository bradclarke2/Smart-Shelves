import Calculations.stockPercentage as stockpercentages
import Graphing.Heatmap as heatmap
import Measurements.MeasureUS as measureUS
import WebPage.API as startAPI
import Objects.XYGrid as XYGridObject
        
ShelfLocations = ["14L8E" , "15R2A"]

XYGridList = XYGridObject.MakeXYGrid()
print (XYGridList)
    
for singleshelfpos in ShelfLocations:
    measureUS.MeasureDistance(singleshelfpos, XYGridList)    
    stockpercentages.UnitsToFill(singleshelfpos, XYGridList)
    heatmap.MakeHeatMap(stockpercentages.shelfHeight, XYGridList, singleshelfpos)
    
startAPI.startfunction()

