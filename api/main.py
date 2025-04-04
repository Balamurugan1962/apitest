from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from llm_api_call import chat

app = Flask(__name__)
cors = CORS(app,origins='*')
api = Api(app)


db = {
    "Bala" : {
        "Age" : 19,
        "Dept" : "CSE"
    },
    "Yukii" : {
        "Age" : 19,
        "Dept" : "CSE"
    },
    "Vasant" : {
        "Age" : 19,
        "Dept" : "Civil"
    }
}

class Hello(Resource):
    def post(self):
        content = request.get_json()
        return jsonify(content)

    def get(self):
        return jsonify({"Hello":"Hiii"})
    

api.add_resource(Hello,'/GetInfo')


@app.route('/')
def start():
    message = chat("Hi")
    print(message)
    return {"LLM Replay": message}

@app.route('/Details',methods = ['GET','POST'])
def details():
    content = request.get_json(silent=True)
    return jsonify(db["Bala"])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
