import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"
    
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = prefix + os.path.join(app.root_path, "data.db")
app.config["SQLALCHEMY_TRCK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model): #表名user 自动生成
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column