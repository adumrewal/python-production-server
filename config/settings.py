import os

class BaseConfig():
    SERVICE_NAME = 'avengers'
    API_PREFIX = f'/{SERVICE_NAME}/v1'
    TESTING = False
    DEBUG = False

class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True

class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'

class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True