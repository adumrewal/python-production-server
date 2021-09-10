import os
import config
from flask import Flask
import json as jsonlibrary

def create_app(test_config=None):
    print(f'Starting app in {config.APP_ENV} environment')

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def home_route():
        return "Hello World"
    
    @app.route(f'{config.API_PREFIX}/health')
    def health_check():
        return jsonlibrary.dumps({'message':config.SERVICE_NAME}), 200, {'Content-Type': 'application/json'}
    
    return app