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
app.config["SQLA"]