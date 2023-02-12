import logging
from flask import request
from timeit import default_timer as timer

import app.services.hero_service as service
from app.middleware.common_context import RequestContext
from app.models.payload_dto import HeroInfoPayloadDTO

def hero_info_api():
    start = timer()

    context = RequestContext()
    payload = request.get_json()
    logging.info({'payload': payload}, extra={**context.logStruct, 'event': 'initiated'})

    try:
        payloadDTO: HeroInfoPayloadDTO = HeroInfoPayloadDTO(payload)
    except Exception as e:
        logging.error({'function': 'controller.hero_info_api', 'error_msg': "Invalid payload: " + str(e)}, extra={**context.logStruct, 'event': 'failure'})
        return "Invalid payload: CL_PARAM_MISSING", 400

    try:
        result = service.hero_info_api(context, payloadDTO)
    except Exception as e:
        logging.error({'function': 'controller.hero_info_api', 'error_msg': str(e)}, extra={**context.logStruct, 'event': 'failure'})
        return "Server Internal Error", 500

    end = timer()
    logging.info({'function': 'controller.hero_info_api', 'duration': str(end-start)}, extra={**context.logStruct, 'event': 'completed'})
    return result
