import logging
from elasticsearch import Elasticsearch

_ES: Elasticsearch = None

def initialize(customConfig=None) -> None:
    global _ES # this is important, to ensure a single connection is made to the es instance

    # customConfig is generally used when using scripts instead of app/flask service
    if customConfig != None:
        host = customConfig.ES_HOST
        username = customConfig.ES_USERNAME
        password = customConfig.ES_PASSWORD
    else:
        try:
            import config
        except ImportError:
            config = None
            logging.error("Elasticsearch config not found")
            return
        host = config.ES_HOST
        username = config.ES_USERNAME
        password = config.ES_PASSWORD
    
    _ES = Elasticsearch(
        [host],
        http_auth=(username, password),
        scheme="https",
    )

    if _ES.ping():
        logging.info("Elasticsearch connection successful")
    else:
        logging.error("Elasticsearch connection not established")
    
    return

def get_es_client(customConfig=None) -> Elasticsearch:
    if _ES == None:
        logging.info("Elasticsearch client requested without initialization")
        initialize(customConfig=customConfig)
    return _ES
