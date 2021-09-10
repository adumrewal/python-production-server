import os
import sys
  
# append the path of the parent directory
sys.path.append("..")

from core.elasticsearch_core import get_es_client
from elasticsearch import helpers
from datetime import datetime

class CustomConfig(object):
  ES_HOST = os.getenv('ES_HOST')
  ES_USERNAME = os.getenv('ES_USERNAME')
  ES_PASSWORD = os.getenv('ES_PASSWORD')


INDEX_NAME_PREFIX = 'hero-info-index-'
NAME_PREFIX = 'hero_info_index'
ES_CLIENT = get_es_client(customConfig=CustomConfig())

def getSettings():
    settings = {
        "number_of_shards": 5,
        "number_of_replicas": 1,
        "default_pipeline": f'{NAME_PREFIX}_pipeline'
    }
    return settings

def getMapping():
    mapping = {
      "dynamic" : "true", # helps with changing the mapping easily in the future. Choose false if don't want to deviate from your mapping.
      "properties" : {
        "basic_info" : {
          "properties" : {
            "name" : {
              "type" : "keyword" # keyword or text are two possibilities for text fields. Look at ES documentation for more details.
            },
            "age" : {
              "type" : "long"
            },
            "planet" : {
              "type" : "keyword"
            }
          }
        },
        "universe" : {
          "properties" : {
            "name" : {
              "type" : "keyword"
            },
            "creator" : {
              "type" : "keyword"
            }
          }
        },
        "power" : {
            "type" : "long"
        },
        "event_time" : {
            "type" : "long"
        }
      }
    }
    return mapping

# Here, we are creating pipeline for injecting data
# This pipeline automatically creates a new index on ES based for a new date in event_time
# For eg.
# if you send event_time 1631282789954 (epoch time in ms), a new index hero-info-index-2021-09-10 will be created and the data will be put in this index
# this makes time based index and searching easy and fast
# this part is not of much relevance to the avengers project, but helps a lot with other services where you receive data on a daily basis
def createPipeline():
    ES_CLIENT.ingest.put_pipeline(
        id=f'{NAME_PREFIX}_pipeline',
        body= {
            'description': 'daily date-time index naming',
            'processors': [
                {
                    'date_index_name': {
                        'field': 'event_time', # refers to the field based on which to create index
                        'date_formats': ['UNIX_MS'],
                        'index_name_prefix': INDEX_NAME_PREFIX, # prefix part of the index name
                        'date_rounding': 'd' # suffix part of the index name
                    }
                }
            ]
        }
    )

def createTemplate():
    ES_CLIENT.indices.put_index_template(
        name=f'{NAME_PREFIX}_template',
        create=True,
        body={
            'index_patterns': [f'{INDEX_NAME_PREFIX}*'],
            'priority': 1,
            'template': {
                'mappings': getMapping(),
                'settings': {
                    'index': getSettings()
                }
            }
        }
    )

def putSampleData():
    doc = {
        'power': '91',
        'event_time': int(datetime.now().timestamp()*1000),
        'basic_info': {
            'name': 'CaptainAmerica',
            'age': 103,
            'planet': 'earth'
        },
        'universe': {
            'name': 'marvel',
            'creator': 'stanley'
        }
    }
    ES_CLIENT.index(index=INDEX_NAME_PREFIX,body=doc)

def putBulkData():
    doc1 = {
        'power': '91',
        'event_time': int(datetime.now().timestamp()*1000),
        'basic_info': {
            'name': 'CaptainAmerica',
            'age': 103,
            'planet': 'earth'
        },
        'universe': {
            'name': 'marvel',
            'creator': 'stanley'
        }
    }
    doc_list = [doc1,doc1]
    helpers.bulk(ES_CLIENT, doc_list, index=INDEX_NAME_PREFIX)


# uncomment the first two for pipeline, template and index creation ⬇️
# uncomment the last two for sample data injection ⬇️

# createPipeline()
# createTemplate()
# putSampleData()
# putBulkData()
