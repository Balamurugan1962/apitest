from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
    return {"message": "Hello By Flask!"}

# hello

if __name__ == "__main__":
    app.run(debug=True)
