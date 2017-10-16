# http://restful-api-design.readthedocs.io/en/latest/resources.html - about REST resources and JSON
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful - designing flask server with REST

# curl -X POST http://127.0.0.1:5002/tracks

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# Flask-RESTful provides a Resource base class that can define the routing for one or more HTTP methods for a given URL.

class Tests(Resource):
    def get(self):
        return "Oslik"

'''
class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
    def post(self):
        return jsonify("Oslik")

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
'''     

api.add_resource(Tests, '/tests') # Route_1

if __name__ == '__main__':
     app.run(port='5002')