from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_restful import Resourse, Api

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

class Hello(Resourse):
    def get(self):
        return jsonify({"Hello":"Hiii"})
    def put(self):
        return jsonify({"Hello":"Hiii"})
    

api.add_resource(Hello,'/GetInfo')

@app.route('/')
def start():
    return {"message": "Hello By Flask! with update"}

@app.route('/Details',methods = ['GET','POST'])
def details():
    content = request.get_json(silent=True)
    return jsonify(db["Bala"])


if __name__ == "__main__":
    app.run(debug=True)
