def startfunction():
    from flask import Flask
    from flask_restful import Resource, Api
    app = Flask(__name__)
    api = Api(app)
    
    class Departmental_Salary(Resource):
        def get(self):
            return 1
    
    api.add_resource(Departmental_Salary, '/measurements/')
    app.run()