from flask import Flask

app = Flask(__name__)

@app.r
def hello('/'):
    return "neo hola"