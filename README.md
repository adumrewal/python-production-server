# Python Production Server
## Flask ✅, Elasticsearch ✅, ElasticAPM ✅, Docker, Logging ✅, Config files ✅

### Dependencies
- Flask: 2.0.1
- Flask_RESTful: 0.3.9
- Elasticsearch: 7.13.4 (I recommend not using 7.14.x as of now. There are some issues with that version when using with python client.)
- elastic_apm: 6.4.0
- ecs_logging: 1.0.1
- blinker: 1.4 (indirect import. `pip install` this incase you face any issues with elasticapm dependencies)


To run this raw flask server, run `python run.py`

#### Detailed Readme coming soon...