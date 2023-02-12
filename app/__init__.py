import os
import config
import logging
from flask import Flask
import json as jsonlibrary

from app.core import elasticsearch_core as es_core
from app.core import observability_core as obs_core
from app.core import logging_core as logs_core
import app.routes.sample_route as sample_route
import app.routes.hero_route as hero_route

logs_core.initialize()

def create_app(test_config=None):
    logging.info(f'Starting app in {config.APP_ENV} environment')

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialise service
    # obs_core.initialize(app=app)
    es_core.initialize()
    sample_route.api.init_app(app=app)
    hero_route.api.init_app(app=app)

    @app.route('/')
    def home_route():
        return "Hello World"
    
    @app.route(f'{config.API_PREFIX}/health')
    def health_check():
        return jsonlibrary.dumps({'message':config.SERVICE_NAME}), 200, {'Content-Type': 'application/json'}
    
    return app
