import logging
import app.dao.elasticsearch_dao as es_dao

# the * means this will do a regular expression based search (on all indexes which start with the prefix hero-info-index-)
HERO_INDEX_NAME = 'hero-info-index-*'

def get_info_for_hero(hero_name=None):
    if hero_name == None or hero_name == "":
        logging.info("None or empty hero_name passed")
        return []
    
    query_body = {
                    "query": {
                        "bool": {
                            "must": [
                                {"match": {"basic_info.name": hero_name}},
                                {"match": {"universe.name": "marvel"}}
                            ]
                        }
                    }
                }
    
    hero_info = es_dao.search(index_name=HERO_INDEX_NAME, search_query=query_body)

    if hero_info == None or len(hero_info) == 0:
        logging.info(f"No hero found with this name: {hero_name}")
        return []
    
    return hero_info
