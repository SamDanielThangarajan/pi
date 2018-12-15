from flask import Flask
from flask_restful import Api, Resource, reqparse

from gpio import switch_on, switch_off

application = Flask(__name__)
api = Api(application)

class GPIO(Resource):
    def get(self, no):
        pass

    def post(self, no):
        switch_on(no)

    def delete(self, no):
        switch_off(no)

    def put(self, no):
        pass

api.add_resource(GPIO, "/gpio/<int:no>", endpoint = 'no')

if __name__ == '__main__':
    application.run(debug=True)
