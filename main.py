from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'Talha'}}

@app.get('/hello')
def hello():
    return {'data':{'hello fastAPi'}}