import config
from flask_restful import Api, Resource
from app.dao.hero_info_dao import get_info_for_hero

api = Api(prefix=config.API_PREFIX)

class HeroInfoAPI(Resource):
   def get(self, hero_name):
       print(f"HeroInfoAPI called with hero_name: {hero_name}")
       
       # this should ideally be routed to a controller or service for handling and result generation
       result = get_info_for_hero(hero_name=hero_name)
       if len(result) == 0:
           return f"Sorry, no hero found with the name: {hero_name}"
       return result[0]

# hero info endpoint
api.add_resource(HeroInfoAPI, '/get_hero_info/<string:hero_name>')