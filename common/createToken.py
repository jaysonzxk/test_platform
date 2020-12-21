from flask import request, jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from module.users import Users
import functools


def create_token(api_user):
    """
    生成token
    :param api_user:
    :return:token
    """
    SECRET_KEY = 'abcdefghijklmm'
    # 第一个参数是内部的私钥，这里写在共用的配置信息里了，如果只是测试可以写死
    # 第二个参数是有效期(秒)
    s = Serializer(SECRET_KEY, expires_in=3600)
    # 接收用户id转换与编码
    token = s.dumps({'name': api_user}).decode('ascii')
    return token


def verify_token(token):
    """
    校验token
    :param token:
    :return:用户信息 or None
    """
    # 参数为私有秘钥，跟上面方法的秘钥保持一致
    SECRET_KEY = 'abcdefghijklmm'
    s = Serializer(SECRET_KEY)
    try:
        # 转为字典
        data = s.loads(token)
    except Exception:
        return None
    # 拿到转换后的数据，根据模型类去数据库查询用户信息
    user = Users.find_by_username(data.get('name'))[0]
    return user


def login_required(view_func):
    SECRET_KEY = 'abcdefghijklmm'

    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            # 在请求头上拿到token
            token = request.headers['x-token']
        except Exception as e:
            # 没接收的到token,给前端抛出错误
            return jsonify({'code': 40004, 'message': '缺少参数token'})

        s = Serializer(SECRET_KEY)
        try:
            s.loads(token)
        except Exception:
            return jsonify({'code': 40005, 'message': '登录已经过期'})
        return view_func(*args, *kwargs)
    return verify_token