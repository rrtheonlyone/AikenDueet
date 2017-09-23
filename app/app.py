from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

import ast

from LZM import compress 
from RLE import decode, encode
from WDE import compressWDE
from BusyTrain import busybody
from sort import qsort

app = Flask(__name__)
api = Api(app)

class Sorting(Resource):
    def get(self):
        return "This is the sorting problem answer"

    def post(self):
    	raw_list = request.get_data()
    	raw_list_string = raw_list.decode("utf-8")

    	raw_list_int = ast.literal_eval(raw_list_string)
    	sorted_list = qsort(raw_list_int)

    	return sorted_list


class StringCompression(Resource):
    def get(self, mode):
        return "This is the String Compression Problem"

    def post(self, mode):
        json_data = request.get_json(force=True)
        string_value = json_data['data']

        if(mode == "LZW"):
            answer = compress(string_value)
        elif(mode == "RLE"):
            answer = decode(encode(string_value))
        else:
            answer = compressWDE(string_value)

        return answer

class TrainPlanner(Resource):
    def get(self, mode):
        return "This is the Train Planner Problem"

    def post(self, mode):
        json_data = request.get_json(force=True)
        destinations = json_data['destinations']
        stations = json_data['stations']
        answer = busybody(destination, stations)

        return answer


api.add_resource(Sorting, '/sort')
api.add_resource(StringCompression, '/stringcompression/<mode>')
api.add_resource(TrainPlanner, '/trainPlanner')



if __name__ == '__main__':
    app.run(debug=True)