import config
import logging
from flask_restful import Api, Resource

api = Api(prefix=config.API_PREFIX)

class SampleAPI(Resource):
    def get(self):
        logging.info("Sample API called")
        return "Sample API of Avengers service"

# sample route endpoint
api.add_resource(SampleAPI, '/sample')