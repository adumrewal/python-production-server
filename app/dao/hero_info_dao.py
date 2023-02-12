import logging

import app.dao.elasticsearch_dao as es_dao
from app.middleware.common_context import RequestContext
from app.models.payload_dto import HeroInfoPayloadDTO

# the * means this will do a regular expression based search (on all indexes which start with the prefix hero-info-index-)
HERO_INDEX_NAME = 'hero-info-index-*'

def get_info_for_hero(context: RequestContext, payloadDTO: HeroInfoPayloadDTO):
    query_body = {
                    "query": {
                        "bool": {
                            "must": [
                                {"match": {"basic_info.name": payloadDTO.hero_name}},
                                {"match": {"universe.name": payloadDTO.universe_name}}
                            ]
                        }
                    }
                }
    
    hero_info = es_dao.search(context, index_name=HERO_INDEX_NAME, body=query_body)

    if hero_info == None or len(hero_info) == 0:
        logging.info({'function': 'hero_info_dao.get_info_for_hero', 'msg': 'No hero found with this name', 'query_body': query_body}, extra={**context.logStruct})
        return []
    
    return hero_info
