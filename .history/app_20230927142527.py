from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route("/user/<name>")
def u1(name):
    return f"{name}"


from markupsafe import escape

@app.route("/user")
def u2(name):
    return f"User: {escape(name)}"