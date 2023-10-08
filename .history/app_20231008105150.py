import os
import sys

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


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


import click


# @app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
# @click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
# def initdb(drop):
#     """Initialize the database."""
#     if drop:  # 判断是否输入了选项
#         db.drop_all()
#     db.create_all()
#     click.echo('Initialized database.')  # 输出提示信息
    
    
    
# def index():
#     user = User.query.first()
#     movies = Movie.query.all()
#     return render_template("index.html", user=user, movies=movies)


@app.cli.command()
def forge():
    db.create_all()
    
    name = "Ray"
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m["title"],year=m["year"])
        db.session.add(movie)
        
    db.session.commit()
    click.echo("Done.")
    
    
def page_not_found(e):
    user = User.query.first()
    return render  