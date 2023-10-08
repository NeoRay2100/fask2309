from flask import Flask
from .models import db  # 从models模块中导入db对象
from flask_sqlalchemy import SQLAlchemy

import sys
import os

app = Flask(__name__)

WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"
    
app.config["SQLALCHEMY_DATABASE_URI"] = prefix + os.path.join(app.root_path, "data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# 其他应用程序配置和路由等
