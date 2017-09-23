from flask import Flask, jsonify, request
from flask_restful import Resource, Api

import ast

from LZM import compress 

app = Flask(__name__)
api = Api(app)

class Sorting(Resource):
    def get(self):
        return "This is the sorting problem answer"

    def post(self):
    	raw_list = request.get_data()
    	raw_list_string = raw_list.decode("utf-8")

    	print(raw_list_string)

    	raw_list_int = ast.literal_eval(raw_list_string)
    	sorted_list = sorted(raw_list_int)

    	print(sorted_list)

    	for i in sorted_list:
    		print(i)

    	return sorted_list


class StringCompression(Resource):
	def get(self, mode):
		return "This is string compression on " + mode

	def post(self, mode):




		# if(mode == "RLE"):

		# else if(mode == LZW):

		# else:



		return "Hello"

api.add_resource(Sorting, '/sort')
api.add_resource(StringCompression, '/stringcompression/<mode>')



if __name__ == '__main__':
    app.run(debug=True)