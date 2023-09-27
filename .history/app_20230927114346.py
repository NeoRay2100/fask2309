from flask import Flask

from apps import create_app

app = Flask(__name__)

@app.route('/')
def hello():
    return "neo hola"