import time

from sqlalchemy import Table, MetaData, Column, Integer, String

from main import db


class Users(db.Model):
    __table__ = Table('users', MetaData(bind=db.engine), autoload=True)

    @staticmethod
    def find_user_by_id(userid):
        row = db.session.query(Users).filter(Users.id==userid).first()
        return row

    @staticmethod
    def find_by_username(username):
        result = db.session.query(Users).filter(Users.username == username).all()
        return result