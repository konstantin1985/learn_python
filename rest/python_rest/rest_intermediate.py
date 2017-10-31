# http://restful-api-design.readthedocs.io/en/latest/resources.html - about REST resources and JSON
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful - designing flask server with REST
# https://onlinehelp.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_fields.htm - fields and resources
# https://stackoverflow.com/questions/30899484/python-flask-calling-functions-using-buttons - flask and buttons
# https://www.w3schools.com/html/html_forms.asp - good article on HTML forms
# https://onlinehelp.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_fields.htm - Another solution on how to use fields in the address

# curl -X POST http://127.0.0.1:5002/todo/api/v1.0/tasks
# curl -X POST -H "Content-Type: application/json" -d '{"title": "third task", "description": "And some description"}' http://127.0.0.1:5002/todo/api/v1.0/tasks // To post JSON

from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse, fields, marshal

app = Flask(__name__)   # Flask application
api = Api(app)          # RESTapi

# Some default tasks that are already present
tasks = [
         { 'id': 1, 'title': u"Learn Rest", 'description': u"It's very important", 'done': False },
         { 'id': 2, 'title': u"Learn Python in general", 'description': u"It's also very important", 'done': False }
         ]

# Template for the marshal function
task_fields = {
               'title': fields.String,
               'description': fields.String,
               'done': fields.Boolean,
               'uri': fields.Url('task') # endpoint in add_resource()
               }

# Resource base class that can define the routing for one or more HTTP methods for a given URL
class TaskListAPI(Resource):
    
    def __init__(self):
    
        # For each resource we define the arguments and how to validate them
        self.reqparse = reqparse.RequestParser()
        
        # Can get values both from 'values' in the html form and 'json' REST request
        self.reqparse.add_argument("title", type = str, required = True,
                                   help = "No task title proveded", location = ['values', 'json'])
        self.reqparse.add_argument('description', type = str, default = "", location = ['values', 'json'])
        
        # Correct way to invoke super in python 2.x
        super(TaskListAPI, self).__init__()
    
    def get(self):
        return {'tasks': [marshal(task, task_fields) for task in tasks]}
    
    def post(self):
        
        # Parse parameters in the post request
        args = self.reqparse.parse_args()
        
        # Add the new received task
        task = {
                'id': tasks[-1]['id'] + 1,
                'title': args['title'],
                'description': args['description'],
                'done': False
                }
        tasks.append(task)
        
        # marshal takes raw data (in the form of a dict, list, object) and a dict of
        # fields to output and filters the data based on those fields.
        return {'task': marshal(task, task_fields)}, 201


class TaskAPI(Resource):
    pass


# If we want a page to be shown properly in the web browser then don't inherit from Resource (it's for REST)
@app.route('/form', methods=['GET'])
def foo():
    return render_template('my_form.html')

# Add all REST API
api.add_resource(TaskListAPI, '/tasks', endpoint = 'tasks')
api.add_resource(TaskAPI, '/tasks/<int:id>', endpoint = 'task')

# 127.0.0.1:5002/form - add new task, html form sends REST POST
# 127.0.0.1:5002/tasks - get all tasks as REST GET, when you write in browser address line GET request is invoked

if __name__ == '__main__':
    app.run(port='5002')
    
# How to kill app on the socket:
# sudo netstat -anp | grep :"5002" // Understand which process is beind the port
# tcp        0      0 127.0.0.1:5003          0.0.0.0:*               LISTEN      8717/python
# sudo kill -9 8717