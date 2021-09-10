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

    ELASTIC_APM_SERVICE_NAME=os.getenv('ELASTIC_APM_SERVICE_NAME')
    ELASTIC_APM_SERVER_URL=os.getenv('ELASTIC_APM_SERVER_URL')
    ELASTIC_APM_SECRET_TOKEN=os.getenv('ELASTIC_APM_SECRET_TOKEN')
    ELASTIC_APM_ENVIRONMENT=os.getenv('ELASTIC_APM_ENVIRONMENT')
    ELASTIC_APM_ENABLED=os.getenv('ELASTIC_APM_ENABLED')

class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    ES_HOST = os.getenv('ES_HOST')
    ES_USERNAME = os.getenv('ES_USERNAME')
    ES_PASSWORD = os.getenv('ES_PASSWORD')

    ELASTIC_APM_SERVICE_NAME=os.getenv('ELASTIC_APM_SERVICE_NAME')
    ELASTIC_APM_SERVER_URL=os.getenv('ELASTIC_APM_SERVER_URL')
    ELASTIC_APM_SECRET_TOKEN=os.getenv('ELASTIC_APM_SECRET_TOKEN')
    ELASTIC_APM_ENVIRONMENT=os.getenv('ELASTIC_APM_ENVIRONMENT')
    ELASTIC_APM_ENABLED=os.getenv('ELASTIC_APM_ENABLED')

class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True