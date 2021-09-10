import config
import blinker # necessary import for elastic apm to work on docker container
from elasticapm.contrib.flask import ElasticAPM

_apm: ElasticAPM = None

def initialize(app) -> None:
    app.config['ELASTIC_APM'] = {
        'SERVICE_NAME': config.ELASTIC_APM_SERVICE_NAME,
        'SECRET_TOKEN': config.ELASTIC_APM_SECRET_TOKEN,
        'ENVIRONMENT': config.ELASTIC_APM_ENVIRONMENT,
        'SERVER_URL': config.ELASTIC_APM_SERVER_URL,
        'ENABLED': config.ELASTIC_APM_ENABLED,
    }

    _apm = ElasticAPM(app)