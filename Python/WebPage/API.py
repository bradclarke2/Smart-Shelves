def startfunction():
    from flask import Flask
    from flask_restful import Resource, Api
    app = Flask(__name__)
    api = Api(app)
    
    class Departmental_Salary(Resource):
        def get(self):
            GridTemp=[]
            for XYGrid in XYGridList:
                GridTemp.append([XYGrid.idpos, XYGrid.xpos, XYGrid.ypos, XYGrid.distance])
            return GridTemp            
 
    
    api.add_resource(Departmental_Salary, '/measurements/')
    app.run()


