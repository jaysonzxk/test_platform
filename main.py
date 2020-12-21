import pymysql
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json

from flask_sqlalchemy import SQLAlchemy

from auto_test.YH.common.logger import Log
from auto_test.YH.run import add_case, run_case

pymysql.install_as_MySQLdb()
app = Flask(__name__, template_folder='templates', static_url_path='/', static_folder='sources')

CORS(app, supports_credentials=True)

# 使用集成方式处理SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234qwer@127.0.0.1:3306/test_platform?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 实例化db对象
db = SQLAlchemy(app)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
#     if request.method == 'POST':
#         data = json.loads(request.get_data(as_text=True))
#         username = data.get('username')
#         password = data.get('password')
#         if username == '' or password == '':
#             return jsonify({'code': 40000, 'message': '用户名和密码不能为空'})
#         elif username == 'admin' and password == '123456':
#             return jsonify({'code': 20000, 'message': '登录成功'})
#         else:
#             return jsonify({'code': 40000, 'message': '用户名或密码错误'})



# @app.route('/home', methods=['GET', 'POST'])
# def home():
#     if request.method == 'GET':
#         return render_template('home.html')
#     if request.method == 'POST':
#         data = json.loads(request.get_data(as_text=True))
#         # rule = data.get('rule')
#         product = data.get('product')
#         module = data.get('module')
#         if product == 'fresh_purchase' and module == 'app_api':
#             Log().info('{}项目-->{}正在执行测试'.format(product, module))
#             all_case = add_case(product, module)
#             run_case(all_case)
#             Log().info('{}项目-->{}自动化执行结束'.format(product, module))
#             return jsonify({'code': 20000, 'message': '执行完成'})
#         elif product == '' or module == '':
#             return jsonify({'code': 30000, 'message': '参数不能为空'})
#         else:
#             return jsonify({'code': 40000, 'message': '参数错误'})


from controller.user import *
app.register_blueprint(user_login, url_prefix='/user')
app.register_blueprint(user_info, url_prefix='/query')

from controller.home import *
app.register_blueprint(homepage, url_prefix='/index')

if __name__ == '__main__':
    app.run(debug=True)
