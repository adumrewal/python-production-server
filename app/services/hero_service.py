import logging

import app.dao.hero_info_dao as dao
from app.middleware.common_context import RequestContext
from app.models.payload_dto import HeroInfoPayloadDTO


# Service layer functions
def hero_info_api(context: RequestContext, payloadDTO: HeroInfoPayloadDTO):
    try:
        result = dao.get_info_for_hero(context, payloadDTO)
    except Exception as e:
        logging.error({'function': 'service.hero_info_api', 'error_msg': str(e)}, extra={**context.logStruct, 'event': 'failure'})
        return "Server Internal Error", 500
    
    if result == None or len(result) == 0:
        return "No hero found with this name", 200

    return result[0], 200
