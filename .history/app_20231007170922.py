# import os
# import sys

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)

# WIN = sys.platform.startswith("win")
# if WIN:
#     prefix = "sqlite:///"
# else:
#     prefix = "sqlite:////"
    

# app.config["SQLALCHEMY_DATABASE_URL"] = prefix + os.path.join(app.root_path, "data.db")
# app.config["SQLALCHEMY_TRCK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)


# class User(db.Model): #表名user 自动生成
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20))
    
# class Movie(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(60))
#     year = db.Column(db.String(4))
    
    
    
    
import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)