app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123@localhost:3306/test' 
#这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名test
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True 
#设置这一项是每次请求结束后都会自动提交数据库中的变动