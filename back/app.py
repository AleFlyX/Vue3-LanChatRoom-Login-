from flask import Flask, request, jsonify,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_socketio import SocketIO, emit ,send
import jwt
import datetime
import secrets
import pymysql

app = Flask(__name__)
# CORS(app, origins=['http://localhost:5173'])  #指定前端地址以允许数据传递
CORS(app, origins=['http://192.168.1.13:5173'])
CORS(app)

socketio = SocketIO(app)

#全局变量

#通知前端获取消息变量
global_toFetch=0


# 配置 MySQL 数据库
# 配置数据库连接 URI
# 格式：mysql://用户名:密码@数据库地址/数据库名称
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:123456@localhost/login_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭 SQLAlchemy 的修改跟踪功能（可选，用于减少资源消耗）
app.config['SECRET_KEY']='ljr666'

db = SQLAlchemy(app)


# 用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False) # 用户名，唯一且不能为空
    password = db.Column(db.String(120), nullable=False) # 密码，不能为空

    # 定义对象的字符串表示形式（可选，用于调试）
    def __repr__(self):
        return f'<User {self.username}>'

# 创建数据库表
with app.app_context():
    db.create_all()

#定义聊天信息模型

#pymysql连接mysql数据库
chatdb_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'db': 'chat',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}



# 登录
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

     # 查询数据库，检查用户名和密码是否匹配, '.first():获取查询结果的第一条记录。'
     #‘=’左边的username是User对象的字段名，格式 字段名=要对比的变量
    user = User.query.filter_by(username=username, password=password).first()

    # 如果用户存在且密码匹配,创建token
    if user:
        usernametk=username
                # 生成 JWT token
        token = jwt.encode({
            'username': usernametk,  # 用户 ID
            'exp': datetime.datetime.now() + datetime.timedelta(hours=1)  # 设置 token 过期时间
        }, app.config['SECRET_KEY'], algorithm='HS256')
        print(token)
        
        # 返回登录成功消息和 token
        return jsonify({
            'message': '登录成功',
            'token': token,
            'user': usernametk,
        }), 200
        # return redirect('http://localhost:5173/home')
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# @app.route('/tokentest',methods=['GET'])
# def send():
#      return jsonify({})

# 注册
@app.route('/api/regist',methods=['POST'])
def regist():
    data=request.get_json()
    newUsername=data.get('username')
    newPassword=data.get('password')

    if not newPassword or not newUsername:
        return jsonify({'message':'请输入账户或密码!'}),400
    
    userExist=User.query.filter_by(username=newUsername).first()
    if userExist:
        return jsonify({'message':'用户已存在,请登录'}),200
    
    #新用户作为对象提交到数据库
    newUser=User(username=newUsername,password=newPassword)
    db.session.add(newUser)
    db.session.commit() 
    return jsonify({'message':'注册成功'}),201

@app.route('/api/send_message', methods=['POST'])
def send_message():
    # 连接到数据库
    connection = pymysql.connect(**chatdb_config)
    data = request.get_json()
    username = data['username']
    message = data['message']
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO messages (username, message) VALUES (%s, %s)"
            cursor.execute(sql, (username, message))
        
        connection.commit()
        return jsonify({'status': 'success'}), 201
    finally:
        connection.close()
 
@app.route('/api/get_messages', methods=['GET'])
def get_messages():
    # 连接到数据库
    connection = pymysql.connect(**chatdb_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM messages ORDER BY id DESC")
            messages = cursor.fetchall()
        
        return jsonify(messages), 200
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)