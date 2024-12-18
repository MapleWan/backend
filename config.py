import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'maplewan'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Qweasd11@@113.45.16.167/maple_data'
    SQLALCHEMY_TRACK_MODIFICATIONS = False