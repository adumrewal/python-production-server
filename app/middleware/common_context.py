import uuid
from flask import request

class RequestContext(object):
    def __init__(self):
        platform = request.headers.get('x-platform') or request.headers.get('X-Platform')
        clientTime = request.headers.get('x-client-time') or request.headers.get('X-Client-Time')
        deviceId = request.headers.get('x-device-id') or request.headers.get('X-Device-Id')
        version = request.headers.get('x-version') or request.headers.get('X-Version')
        authId = request.headers.get('x-auth-id') or request.headers.get('X-Auth-Id')
        request_id = request.headers.get('x-request-id') or request.headers.get('X-Request-Id') or str(uuid.uuid4())
        
        headers = {
            'platform': platform,
            'device_id': deviceId,
            'version': version,
            'client_time': clientTime,
        }
        
        logStruct = {
            'topic': 'request',
            'request_id': request_id,
            'http_method': request.method,
            'uri': request.path,
        }
        
        if platform:
            logStruct['platform'] = platform
        if clientTime:
            logStruct['client_time'] = clientTime
        if deviceId:
            logStruct['device_id'] = deviceId
        if version:
            logStruct['version'] = version
        if authId:
            logStruct['auth_id'] = authId

        
        self.requestId = request_id
        self.logStruct = logStruct
        self.headers = headers
        self.authId = authId

        request.context = self
        return
