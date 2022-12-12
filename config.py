# insert config info for database connection
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # if environment variables present, secret key and db are set to following:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # if env presnet, this sets sqlalchemy db to specified env variable, if not to sqlite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # this prevents modification tracking