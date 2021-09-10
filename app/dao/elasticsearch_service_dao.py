from pprint import pprint
import logging
from elasticsearch.helpers import bulk
from app.core.elasticsearch_core import get_es_client

def search(index_name, search_query, size=9999):
    _ES = get_es_client()
    res = _ES.search(index=index_name, body=search_query, size=size)

    hits = res['hits']['total']['value']
    if hits>size:
        return search(index_name=index_name, search_query=search_query, size=size*10)
    
    logging.info("ES Search success, got %d Hits" % hits) if res != None else logging.info("Error: ES Search unsuccessful")
    res = res['hits']['hits']
    if res != None:
        return res
    return None

def put_single_doc(index_name, doc):
    _ES = get_es_client()
    res = _ES.index(index=index_name, body=doc)
    pprint(res)
    return

def put_bulk(index_name, doc_list):
    _ES = get_es_client()
    res = bulk(_ES, doc_list, index=index_name)
    pprint(res.count)
    return