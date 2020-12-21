import json
import jwt
from module.users import Users
from flask import Blueprint, request, render_template, jsonify, redirect, url_for
from common.createToken import create_token, login_required, verify_token



homepage = Blueprint('home', __name__)


@homepage.route('/homepage', strict_slashes=False)
# @login_required
def home():
    """
    主页
    :return:
    """
    token = request.headers['x-token']
    user = verify_token(token)
    data = {
        'username': user.username
    }
    return render_template('home.html')


