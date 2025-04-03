from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def start():
    return {"messege" : "Hello World!"}