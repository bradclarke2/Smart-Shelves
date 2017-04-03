import Objects.XYGrid as XYGridObject
import Objects.shelf as ShelfObject
import Calculations.stockPercentage as stockpercentages
import Measurements.MeasureUS as measureUS
import Graphing.Heatmap as heatmap
import Objects.product as ProductObject
import InsertDB as insertDB

def startfunction():
    from flask import Flask
    from flask_restful import Resource, Api
    app = Flask(__name__)
    api = Api(app)
    
    class Departmental_Salary(Resource):
        def get(self):
            ProductList = ProductObject.makeProductGrid()
            XYGridList = XYGridObject.MakeXYGrid()
            ShelfList = ShelfObject.makeShelfGrid()
            for singleshelf in ShelfList:
                measureUS.MeasureDistance(singleshelf, XYGridList) 
                stockpercentages.UnitsToFill(singleshelf, ProductList, XYGridList)
                heatmap.MakeHeatMap(singleshelf.height, XYGridList, singleshelf.location)
            print("XYGrid=")
            for XYGrid in XYGridList:
                print(XYGrid.shelflocation,",",XYGrid.idpos,",",XYGrid.xpos,",",XYGrid.ypos,",",XYGrid.distance)
            print("ShelfGrid=")
            for Shelf in ShelfList:
                print(Shelf.location,",",Shelf.height,",",Shelf.width,",",Shelf.depth,",",Shelf.volumePercentFull,",", Shelf.areaFull,",",Shelf.unitsOfSpace)
            return singleshelf.unitsOfSpace
                 
    class list_priority(Resource):
        def get(self):
            ProductList = ProductObject.makeProductGrid()
            XYGridList = XYGridObject.MakeXYGrid()
            ShelfList = ShelfObject.makeShelfGrid()
            for singleshelf in ShelfList:
                measureUS.MeasureDistance(singleshelf, XYGridList)        
                stockpercentages.UnitsToFill(singleshelf, ProductList, XYGridList)      
                print(singleshelf.location, "is", singleshelf.volumePercentFull*100, "% full and can fit", singleshelf.unitsOfSpace, "more units of X")
                heatmap.MakeHeatMap(singleshelf, XYGridList)              
                insertDB.insertShelfRecord(singleshelf)
                heatmap.MakeSalesGraph(singleshelf)
            #insertDB.printShelfDB()
            prioritisedFillList = stockpercentages.calculateFillListOrder(ShelfList)
            return prioritisedFillList
         
    api.add_resource(Departmental_Salary, '/measurements/')
    api.add_resource(list_priority, '/list/')
    
    app.run()