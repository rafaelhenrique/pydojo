from decouple import config


class BaseConfig(object):
    SITE_NAME = 'Cool Editor'
    SECRET_KEY = config('SECRET_KEY')
    SERVER_NAME = config('SERVER_NAME')
    LOGENABLE = True
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URI')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_ECHO = True


class TestConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pydojo.sqlite3'


class ProductionConfig(BaseConfig):
    ASSETS_DEBUG = False
    WTF_CSRF_ENABLED = True
