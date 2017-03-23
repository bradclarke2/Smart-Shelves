from Main.main import XYGridList, ShelfList
import Calculations

def startfunction():
    from flask import Flask
    from flask_restful import Resource, Api
    app = Flask(__name__)
    api = Api(app)
    
    class Departmental_Salary(Resource):
        def get(self):
            for singleshelfpos in ShelfList:
                return Calculations.stockPercentage.UnitsToFill(singleshelfpos, XYGridList)      
 
    api.add_resource(Departmental_Salary, '/measurements/')
    app.run()