import json
import jwt
from module.users import Users
from flask import Blueprint, request, render_template, jsonify
from common.createToken import create_token, login_required, verify_token

user_login = Blueprint('login', __name__)
user_info = Blueprint('userInfo', __name__)




@user_login.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    user = Users()
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        username = data.get('username')
        password = data.get('password')
        try:
            name = user.find_by_username(username)[0].username
            pwd = user.find_by_username(username)[0].password
        except Exception as e:
            return jsonify({'code': 40001, 'message': '查询用户信息失败'})
        if name is None and password == pwd:
            return jsonify({'code': 40002, 'message': '用户名不能为空'})
        if name is not None and password != pwd:
            return jsonify({'code': 40003, 'message': '用户名或密码错误'})

        # 获取用户id，传入生成token的方法，并接收返回的token
        if name is not None and password == pwd:
            token = create_token(name)
            return jsonify({'code': 20000, 'message': '登录成功', 'token': token})


@user_info.route('/userInfo', strict_slashes=False)
@login_required
def userInfo():
    """
    登录用户信息
    :return:
    """
    token = request.headers['x-token']
    user = verify_token(token)

    data = {
        'username': user.username,
        'email': user.email
    }
    return jsonify({'code': 20000, 'message': '成功', 'data': data})


