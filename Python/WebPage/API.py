import Objects.XYGrid as XYGridObject
import Objects.shelf as ShelfObject
import Calculations.stockPercentage as stockpercentages
import Measurements.MeasureUS as measureUS
import Graphing.Heatmap as heatmap
import Objects.product as ProductObject


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
                 
    class location(Resource):
        def get(self):   
            return 1 
    
    class picture_regen(Resource):
        def get(self):
            return 2
 
    api.add_resource(Departmental_Salary, '/measurements/')
    api.add_resource(location, '/shelflocation/')
    api.add_resource(picture_regen, '/pictureregen/')
    app.run()