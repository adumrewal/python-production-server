import redis
import logging

import config

_REDIS_SERVER_INST: redis.Redis = None


def initialize() -> redis.Redis:
    '''Get redis server instance, if not created, create one'''
    global _REDIS_SERVER_INST
    if not _REDIS_SERVER_INST:
        _REDIS_SERVER_INST = redis.Redis.from_url(config.REDIS_URI)
    
    if _REDIS_SERVER_INST:
        logging.info({'message': 'Redis server initialized successfully'})

def get_redis_server():
    global _REDIS_SERVER_INST
    if not _REDIS_SERVER_INST:
        logging.info({'message': 'Redis server requested without initialization'})
        initialize()
    return _REDIS_SERVER_INST
