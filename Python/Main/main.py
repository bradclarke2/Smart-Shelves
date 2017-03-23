import Calculations.stockPercentage as stockpercentages
import Graphing.Heatmap as heatmap
import Measurements.MeasureUS as measureUS
import Objects.XYGrid as XYGridObject
import Objects.shelf as ShelfObject
import WebPage

XYGridList = XYGridObject.MakeXYGrid()
ShelfList = ShelfObject.makeShelfGrid()

for singleshelfpos in ShelfList:
    print(singleshelfpos.location)
    measureUS.MeasureDistance(singleshelfpos.location, XYGridList)    
    stockpercentages.UnitsToFill(singleshelfpos.location, XYGridList)
    heatmap.MakeHeatMap(stockpercentages.shelfHeight, XYGridList, singleshelfpos.location)
    
WebPage.API.startfunction()