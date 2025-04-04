from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from llm_api_call import chat

app = Flask(__name__)
cors = CORS(app,origins='*')
api = Api(app)

ChatWithAi_post_args = reqparse.RequestParser()
ChatWithAi_post_args.add_argument("Type",type=str,help="Either user or system")
ChatWithAi_post_args.add_argument("Message",type=str,help="Messege to send llm's",required = True)

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

class ChatWithAi(Resource):
    def post(self):
        args = ChatWithAi_post_args.parse_args()
        reply = chat(args["Message"])
        return jsonify({"reply" : reply})

    def get(self):
        return jsonify({"Hello":"Hiii"})
    

api.add_resource(ChatWithAi,'/ChatWithAi')


@app.route('/')
def start():
    message = chat("Hi")
    print(message)
    return jsonify({"LLM Replay": message})

@app.route('/Details',methods = ['GET','POST'])
def details():
    content = request.get_json(silent=True)
    return jsonify(db["Bala"])


if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5001")
