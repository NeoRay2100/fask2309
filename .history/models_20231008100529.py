import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# WIN = sys.platform.startswith('win')
# if WIN:  
#     prefix = 'sqlite:///'
# else:  
#     prefix = 'sqlite:////'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/test' 
#这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名test
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True 
#设置这一项是每次请求结束后都会自动提交数据库中的变动
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)





class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份