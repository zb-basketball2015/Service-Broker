from flask import Flask
from service_broker.http_client import host, port, username, password, do_request
##############

app = Flask('service-broker')

token = None

@app.route('/v2/catalog')
def list_services():

    global token

    headers = {
        'username':username,
        'password':password
    }

    url = 'http://' + host + port + ':' + '/services'

    try:
        result, status_code = do_request('get', url, None, headers, None)
        token = result['token_expiration'].encode('utf-8')
    except Exception, e:
        print e

    # params = None
    # http_client = None
    # try:
    #     http_client = httplib.HTTPConnection()
    #     http_client.request('get', '/services', params, )
    #     response = http_client.getresponse().read()
    #     results = json.loads(response)
    #     token = results['token_expiration'].encode('utf-8')
    # except Exception, e:
    #     print e
    # finally:
    #     if http_client:
    #         http_client.close()
    pass

@app.route('/v2/service_instances/<instance_id>', methods=['PUT'])
def provision_instance():

    global token

    headers = {
        'username':username,
        'password':password,
        'token': token
    }

    url = 'http://' + host + port + ':' + '/instances'

    try:
        result, status_code = do_request('post', url, None, headers, None)
    except Exception, e:
        print e
    pass

@app.route('/v2/service_instances/<instance_id>', methods=['PATCH'])
def update_instance():

    global token

    headers = {
        "name": "update",
        "parameters": {
            'username':username,
            'password':password,
            'token': token
        }
    }

    url = 'http://' + host + port + ':' + '/instances/<instance_id>/update'

    try:
        result, status_code = do_request('post', url, None, headers, None)
    except Exception, e:
        print e
    pass

@app.route('/v2/service_instances/<instance_id>/service_bindings/<binding_id>', methods=['PUT'])
def bind_instance():

    global token

    headers = {
        "name": "bind",
        "parameters": {
            'username':username,
            'password':password,
            'token': token
        }
    }

    url = 'http://' + host + port + ':' + '/instances/<instance_id>/bind'

    try:
        result, status_code = do_request('post', url, None, headers, None)
    except Exception, e:
        print e
    pass

@app.route('/v2/service_instances/<instance_id>/service_bindings/<binding_id>', methods=['DELETE'])
def unbind_instance():

    global token

    headers = {
        "name": "unbind",
        "parameters": {
            'username':username,
            'password':password,
            'token': token
        }
    }

    url = 'http://' + host + port + ':' + '/instances/<instance_id>/unbind'

    try:
        result, status_code = do_request('post', url, None, headers, None)
    except Exception, e:
        print e
    pass

@app.route('/v2/service_instances/<instance_id>', methods=['DELETE'])
def deprovision_instance():

    global token

    headers = {
        'username':username,
        'password':password,
        'token': token
    }

    url = 'http://' + host + port + ':' + '/instances/<instance_id>'

    try:
        result, status_code = do_request('delete', url, None, headers, None)
    except Exception, e:
        print e
    pass

@app.route('/v2/service_instances/<instance_id>/last_operation')
def get_last_operation():

    global token

    headers = {
        'username':username,
        'password':password,
        'token': token
    }

    url = 'http://' + host + port + ':' + '/instances/<instance_id>/actions'

    try:
        result, status_code = do_request('post', url, None, headers, None)
    except Exception, e:
        print e
    pass
