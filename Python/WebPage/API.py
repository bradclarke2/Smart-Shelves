from flask import Flask, request
from flask_restful import Resource, Api

def start_api():
    app = Flask(__name__)
    api = Api(app)
    
    class Departmental_Salary(Resource):
        def get(self, department_name):
            return department_name
     
    api.add_resource(Departmental_Salary, '/dept/<string:department_name>')
    
    app.run()