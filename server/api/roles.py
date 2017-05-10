from flask_restful import Resource, reqparse, fields, marshal
from utils import auth, get_resource

key = 'role'

data = [
    {'id': 1, 'name':'Admin'},
    {'id': 2, 'name':'Employee'},
]

fields = {
    'name': fields.String,
    'uri': fields.Url(key, absolute=True)
}


class RoleListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   help='No {} name provided'.format(key),
                                   location='json')
        super().__init__()

    def get(self):
        return {key + 's': [marshal(r, fields) for r in data]}

    def post(self):
        args = self.reqparse.parse_args()
        r = {'id': data[-1]['id'] + 1}
        for k in fields:
            if k != 'uri' and k in args:
                r[k] = args[k]
        data.append(r)
        return {key: marshal(r, fields)}, 201


class RoleAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.key = 'role'
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json')
        super().__init__()

    def get(self, id):
        r = get_resource(data, id)
        return {key: marshal(r, fields)}

    def put(self, id):
        r = get_resource(data, id)
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                r[k] = v
        return {key: marshal(r, fields)}

    def delete(self, id):
        r = get_resource(data, id)
        data.remove(r)
        return {'result': True}
