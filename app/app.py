from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Sorting(Resource):

    def get(self):
        return "This is the sorting problem answer"

    def post(self):
    	raw_list = request.get_data()
    	print(list(name))

    	return "test"

api.add_resource(Sorting, '/')



if __name__ == '__main__':
    app.run(debug=True)