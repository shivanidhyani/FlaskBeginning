from flask import Flask, request
from flask_restful import Resource, Api
import requests
from werkzeug.wrappers import response

app = Flask(__name__)
api = Api(app)

class api1(Resource):
    def __init__(self):
        pass

    def post(self):
        data = request.get_json(force=True)
        print(data)
        name = data["name"] 
        weight = data["weight"] 
        height = data["height"] 

        weight = float(weight/1000)
        height = float(0.3048*height)

        data = {
            "weight" : weight,
            "heights" : height
        }

        response = requests.post('http://127.0.0.1:5001/bmi',data)

        print(response.text)
        result = {
            'result' : str(name)+' you are '+str(response.Category)
        }

        return result

api.add_resource(api1, '/conversion')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
