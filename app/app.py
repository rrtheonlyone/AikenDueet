from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

import ast

from LZM import compress 
from RLE import compress1
from WDE import compressWDE
from BusyTrain import busybody
from sort import qsort

app = Flask(__name__)
api = Api(app)

class Sorting(Resource):
    def get(self):
        return jsonify({"Sort": 12})

    def post(self):
    	return qsort(request.get_json(force=True))

class JewelleryHeist(Resource):
    def get(self):
        return "This is the Jewellery Heist Problem"

    def post(self):
        json_data = request.get_json(force=True)
        weight = json_data["weight"]
        vault = json_data["vault"]

        answer = fakeknapsack(vault, weight)
        answer_json = {"heist": answer}
        return jsonify(answer_json) 

class StringCompression(Resource):
    def get(self, mode):
        return "This is the String Compression Problem"

    def post(self, mode):
        json_data = request.get_json(force=True)
        string_value = json_data['data']

        if(mode == "LZW"):
            answer = compress(string_value)
        elif(mode == "RLE"):
            answer = compress1(string_value)
        else:
            answer = compressWDE(string_value)

        return answer

class ReleaseScheduler(Resource):
    def get(self):
        return "This is the Release Scheduler Problem"

    def post(self):
        raw_list = request.get_data()
        raw_list_string = raw_list.decode("utf-8")
        answer = ast.literal_eval(raw_list_string)

        return answer

class TrainPlanner(Resource):
    def get(self):
        return "This is the Train Planner Problem"

    def post(self):
        json_data = request.get_json(force=True)
        destination = json_data['destination']
        stations = json_data['stations']
        answer = busybody(destination, stations)

        return answer



api.add_resource(Sorting, '/sort')
api.add_resource(StringCompression, '/stringcompression/<mode>')
api.add_resource(TrainPlanner, '/trainPlanner')
api.add_resource(JewelleryHeist, '/heist')
api.add_resource(ReleaseScheduler, '/releaseSchedule')


if __name__ == '__main__':
    app.run(debug=True)