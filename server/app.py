from flask import Flask, make_response, jsonify
from flask_restful import Api
from api.roles import RoleAPI, RoleListAPI
from api.projects import ProjectAPI, ProjectListAPI
from api.users import UserAPI, UserListAPI
from api.tasks import TaskAPI, TaskListAPI
from api.trackings import TrackingAPI, TrackingListAPI

app = Flask(__name__)
api = Api(app)

app.config.update(
    DEBUG = True,
    SECRET_KEY = 'T!kAl rulzz'
)

api.add_resource(RoleListAPI, '/jattul/api/v1.0/roles', endpoint='roles')
api.add_resource(RoleAPI, '/jattul/api/v1.0/roles/<int:id>', endpoint='role')
api.add_resource(UserListAPI, '/jattul/api/v1.0/users', endpoint='users')
api.add_resource(UserAPI, '/jattul/api/v1.0/users/<int:id>', endpoint='user')
api.add_resource(TaskListAPI, '/jattul/api/v1.0/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/jattul/api/v1.0/tasks/<int:id>', endpoint='task')
api.add_resource(ProjectListAPI, '/jattul/api/v1.0/projects', endpoint='projects')
api.add_resource(ProjectAPI, '/jattul/api/v1.0/projects/<int:id>', endpoint='project')
api.add_resource(TrackingListAPI, '/jattul/api/v1.0/trackings', endpoint='trackings')
api.add_resource(TrackingAPI, '/jattul/api/v1.0/trackings/<int:id>', endpoint='tracking')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

# @app.route('/jattul/api/v1.0/login', methods=['GET'])
# def login():
#     return '', 401

if __name__ == '__main__':
    app.run()