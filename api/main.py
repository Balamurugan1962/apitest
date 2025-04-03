from flask import Flask,request,jsonify
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app,origins='*')

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

@app.route('/')
def start():
    return {"message": "Hello By Flask!"}

@app.route('/Details',methods = ['GET','POST'])
def details():
    content = request.get_json(silent=True)
    return jsonify(db["Bala"])


if __name__ == "__main__":
    app.run(debug=True)
