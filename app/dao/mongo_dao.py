import config

from app.core.mongo_core import get_client

def get_collection(collection_name=config.MONGO_COLLECTION_NAME):
    '''Get a collection from the database'''
    client = get_client()
    db = client[config.MONGO_DB_NAME]
    collection = db[collection_name]
    return collection

def add(doc_json):
    '''Add a document to the database
    
    Args:
        doc_json (dict): The document to add to the database
    '''
    NAcSession = get_collection()
    NAcSession.insert_one(doc_json)

def get(query):
    '''Get a document from the database
    
    Args:
        query (dict): The query to use to find the document
    '''
    NAcSession = get_collection()
    trip_doc = NAcSession.find_one(query, max_time_ms=1000)
    return trip_doc

def update(query,values):
    '''Update a document in the database
    
    Args:
        query (dict): The query to use to find the document
        values (dict): The values to update the document with
    '''
    NAcSession = get_collection()
    NAcSession.update_one(query,values)

def delete(query):
    '''Delete a document from the database
    
    Args:
        query (dict): The query to use to find the document
    '''
    NAcSession = get_collection()
    NAcSession.delete_one(query)
