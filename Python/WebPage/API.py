import Calculations

def startfunction():
    from flask import Flask
    from flask_restful import Resource, Api
    app = Flask(__name__)
    api = Api(app)
    
    class Departmental_Salary(Resource):
        def get(self):
#             for singleshelfpos in ShelfList:
#                 return Calculations.stockPercentage.UnitsToFill(singleshelfpos, XYGridList)   
            return 1
          
    class location(Resource):
        def get(self):
#             for singleshelfpos in ShelfList:
#                 return Calculations.stockPercentage.UnitsToFill(singleshelfpos, XYGridList)   
            return 2 
 
    api.add_resource(Departmental_Salary, '/measurements/')
    api.add_resource(location, '/shelflocation/')
    app.run()