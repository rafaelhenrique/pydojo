from decouple import config


class BaseConfig(object):
    SITE_NAME = 'Cool Editor'
    SECRET_KEY = config('SECRET_KEY')
    SERVER_NAME = config('SERVER_NAME')
    LOGENABLE = True
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = True


class TestConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    ASSETS_DEBUG = False
    WTF_CSRF_ENABLED = True
