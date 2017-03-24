import Calculations.stockPercentage as stockpercentages
import Graphing.Heatmap as heatmap
import Measurements.MeasureUS as measureUS
import Objects.XYGrid as XYGridObject
import Objects.shelf as ShelfObject
import Objects.product as ProductObject
import WebPage.API as test

ProductList = ProductObject.makeProductGrid()
XYGridList = XYGridObject.MakeXYGrid()
ShelfList = ShelfObject.makeShelfGrid()

for singleshelf in ShelfList:
    measureUS.MeasureDistance(singleshelf, XYGridList)        
    stockpercentages.UnitsToFill(singleshelf, ProductList, XYGridList)

    print(singleshelf.location, "is", singleshelf.volumePercentFull*100, "% full and can fit", singleshelf.unitsOfSpace, "more units of X")
    heatmap.MakeHeatMap(singleshelf.height, XYGridList, singleshelf.location)

print("XYGrid=")
for XYGrid in XYGridList:
    print(XYGrid.shelflocation,",",XYGrid.idpos,",",XYGrid.xpos,",",XYGrid.ypos,",",XYGrid.distance)

print("ShelfGrid=")
for Shelf in ShelfList:
    print(Shelf.location,",",Shelf.height,",",Shelf.width,",",Shelf.depth,",",Shelf.volumePercentFull,",", Shelf.areaFull,",",Shelf.unitsOfSpace)

print("ProductList")
for Product in ProductList:
    print(Product.name, ",", Product.tpnb, ",",Product.height, ",",Product.width, ",",Product.depth, ",",Product.weight)


test.startfunction()