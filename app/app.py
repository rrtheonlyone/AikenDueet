from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

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
        return "This is the String Compression Problem"

    def post(self, mode):
        json_data = request.get_json(force=True)
        string_value = json_data['data']

        answer = compress(string_value);

        return answer


api.add_resource(Sorting, '/sort')
api.add_resource(StringCompression, '/stringcompression/<mode>')



if __name__ == '__main__':
    app.run(debug=True)