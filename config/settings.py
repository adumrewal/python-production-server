import os

class BaseConfig():
    SERVICE_NAME = 'avengers'
    API_PREFIX = f'/{SERVICE_NAME}/v1'
    TESTING = False
    DEBUG = False

class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    ES_HOST = os.getenv('ES_HOST')
    ES_USERNAME = os.getenv('ES_USERNAME')
    ES_PASSWORD = os.getenv('ES_PASSWORD')

class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    ES_HOST = os.getenv('ES_HOST')
    ES_USERNAME = os.getenv('ES_USERNAME')
    ES_PASSWORD = os.getenv('ES_PASSWORD')

class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True