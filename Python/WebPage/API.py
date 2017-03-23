import Objects.XYGrid as XYGridObject
import Objects.shelf as ShelfObject
import Calculations.stockPercentage as stockpercentages
import Measurements.MeasureUS as measureUS

def startfunction():
    from flask import Flask
    from flask_restful import Resource, Api
    app = Flask(__name__)
    api = Api(app)
    
    class Departmental_Salary(Resource):
        def get(self):
            XYGridList = XYGridObject.MakeXYGrid()
            ShelfList = ShelfObject.makeShelfGrid()
            for singleshelfpos in ShelfList:
                measureUS.MeasureDistance(singleshelfpos.location, XYGridList) 
                a =stockpercentages.UnitsToFill(singleshelfpos.location, XYGridList)
                print(a)
            return a
          
    class location(Resource):
        def get(self):   
            return 2 
 
    api.add_resource(Departmental_Salary, '/measurements/')
    api.add_resource(location, '/shelflocation/')
    app.run()