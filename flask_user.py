from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

userss = {
    '1': {
        'name': 'Ваня',
        'age': '30'
    },
    '2': {
        'name': 'Петя',
        'age': '20'
    }
}

class Users(Resource):
    def get(self):
        return {'data': userss}, 200

api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run()

