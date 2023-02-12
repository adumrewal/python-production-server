import config
from flask_restful import Api, Resource

import app.controller.hero_controller as controller

api = Api(prefix=config.API_PREFIX)

class HeroInfoAPI(Resource):
    def post(self):
        return controller.hero_info_api()


# hero_info_api endpoint
api.add_resource(HeroInfoAPI, '/hero_info')
