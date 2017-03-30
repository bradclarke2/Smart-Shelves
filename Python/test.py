from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import json

import json

app = Flask(__name__)
api = Api(app)

class Departments_Meta(Resource):
    def get(self):
        return 1

class Departmental_Salary(Resource):
    def get(self, department_name):
        return department_name
    
class Testings(Resource):
    def get(self, department_name):
        
        d = {}
        d["Name"] = "Luke"
        d["Country"] = "Canada"
 
        b = json.dumps(d, ensure_ascii=False)
        
        return b
 
api.add_resource(Departmental_Salary, '/dept/<string:department_name>')
api.add_resource(Departments_Meta, '/departments')
api.add_resource(Testings, '/tests/<string:department_name>')

if __name__ == '__main__':
    app.run()