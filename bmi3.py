from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class api3(Resource):
    def __init__(self):
        pass

    def post(self):
        data = request.get_json(force=True)
        print(data)
        score = data["score"]

        if score<18.5:
            result = {
                'Category' : 'UnderWeight'
            }
        elif 18.5 < score < 25:
            result = {
                'Category' : 'Average'
            }
        elif 25 < score < 30:
            result = {
                'Category' : 'OverWeight'
            }
        elif score > 30:
            result = {
                'Category' : 'Obese'
            }
        
        return result

api.add_resource(api3, '/score')

if __name__ == "__main__":
    app.run(debug=True, port=5002)
