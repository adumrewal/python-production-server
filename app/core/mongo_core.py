import config
import logging
from pymongo import MongoClient

_MONGO_CLIENT = None


def initialize():
    '''Initialize the client connection object'''
    global _MONGO_CLIENT
    mongo_url = 'mongodb://{}:{}@{}/{}?authSource=admin&retryWrites=true'.format(
        config.MONGODB_USER, 
        config.MONGODB_PASSWORD, 
        config.MONGODB_URI, 
        config.MONGO_DB_NAME)
    _MONGO_CLIENT = MongoClient(mongo_url, maxPoolSize=25)

def get_client():
    '''Get the client connection object'''
    global _MONGO_CLIENT
    if _MONGO_CLIENT == None:
        logging.info({'message': 'MongoDB client requested without initialization'})
        initialize()
    return _MONGO_CLIENT
