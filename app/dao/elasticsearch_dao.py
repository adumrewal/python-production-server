import logging
from elasticsearch.helpers import bulk
from app.core.elasticsearch_core import get_es_client

def search(context={}, index_name=None, body=None, fields=None, size=1e4):
    """Elasticsearch index search method.

    Args:
        context (dict): Context dictionary for logging.
        index_name (str, optional): ES index name to search. Can contain * for multiple indices. Defaults to None.\n
        body (dict, optional): Elastic query dictionary. Defaults to None. Sample keys for dict can be as follows:\n
        body = {
            "query": dict,
            "sort": dict
        }\n
        fields (list, optional): Fields to include in search result. Defaults to None.
        size (int, optional): Current code fetches all possible results with each page of length `size`. Defaults to 9999.

    Returns:
        list: If result exists returns a list of results, else returns empty list.
    """
    es_client = get_es_client()
    
    result = []
    while True:
        res = es_client.search(
            index=index_name,
            body=body,
            _source_includes=fields,
            size=size)

        res = res['hits']['hits'] # get the actual hits
        result.extend(res)

        if size != 1e4: # if size is not 1e4, then we are not doing a scroll search
            break
        if len(res) == 0 or len(res) < size: # if we have reached the end of the search
            break
        body['search_after'] = res[-1]['sort']
    
    logging.info({'message': 'ES search success', 'count_hits': len(result)}, extra=context)
    return result

def put_single_doc(context={}, index_name=None, doc={}):
    """Elasticsearch index put method.
    
    Args:
        context (dict): Context dictionary for logging.
        index_name (str, optional): ES index name to search. Can contain * for multiple indices. Defaults to None.
        doc (dict, optional): Document to be indexed. Defaults to {}.
    
    Returns:
        None: Returns None.
    """
    _ES = get_es_client()
    res = _ES.index(index=index_name, body=doc)
    if res!=None:
        logging.debug({'message': 'ES put_single_doc success', 'res': res}, extra=context)
    else:
        logging.debug({'message': 'Error: ES put_single_doc unsuccessful', 'res': res}, extra=context)
    return

def put_bulk(context={}, index_name=None, doc_list=[]):
    """Elasticsearch bulk index put method.

    Args:
        context (dict, optional): Context dictionary for logging.. Defaults to {}.
        index_name (_type_, optional): ES index name to search. Can contain * for multiple indices. Defaults to None.
        doc_list (list, optional): List of documents to be indexed. Defaults to [].
    
    Returns:
        None: Returns None.
    """
    _ES = get_es_client()
    res = bulk(_ES, doc_list, index=index_name)
    if res != None:
        logging.debug({'message': 'ES put_bulk success', 'res': res}, extra=context)
    else:
        logging.debug({'message': 'Error: ES put_bulk unsuccessful', 'res': res}, extra=context)
    return
