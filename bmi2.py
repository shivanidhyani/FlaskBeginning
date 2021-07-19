from flask import Flask, request
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class api2(Resource):
    def __init__(self):
        pass

    def post(self):
        data = request.get_json(force=True)
        print(data)
        weight = data["weight"] 
        height = data["height"] 

        score = weight/(height)**2
        response = requests.post('http://127.0.0.1:5002/score',data={"score":score})
        print("API 2 Response")
        print(response.text)
        return response

api.add_resource(api2, '/bmi')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
