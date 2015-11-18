from flask import Flask
import urllib, httplib
import json

##############

app = Flask('service-broker')

token = None

@app.route('/v2/catalog')
def list_services():
    global token
    username = 'admin'
    password = 'dangerous'
    params = None
    http_client = None
    headers = {
        "username": username,
        "password": password
    }
    try:
        http_client = httplib.HTTPConnection()
        http_client.request('get', '/services', params, headers)
        response = http_client.getresponse().read()
        results = json.loads(response)
        token = results['token_expiration'].encode('utf-8')
    except Exception, e:
        print e
    finally:
        if http_client:
            http_client.close()
    pass

@app.route('/v2/service_instances/<instance_id>', methods=['PUT'])
def provision_instance(instance_id):
    global token
    http_client = None
    headers = {
        "token": token,
        "instance_id": instance_id
    }

    pass

@app.route('/v2/service_instances/<instance_id>', methods=['PATCH'])
def update_instance(instance_id):
    global token
    http_client = None
    headers = {
        "token": token,
        "instance_id": instance_id
    }
    pass

@app.route('/v2/service_instances/<instance_id>/service_bindings/<binding_id>', methods=['PUT'])
def bind_instance(instance_id, binding_id):
    global token
    http_client = None
    headers = {
        "token": token,
        "instance_id": instance_id,
        "binding_id": binding_id
    }
    pass

@app.route('/v2/service_instances/<instance_id>/service_bindings/<binding_id>', methods=['DELETE'])
def unbind_instance(instance_id, binding_id):
    global token
    http_client = None
    headers = {
        "token": token,
        "instance_id": instance_id,
        "binding_id": binding_id
    }
    pass

@app.route('/v2/service_instances/<instance_id>', methods=['DELETE'])
def deprovision_instance(instance_id):
    global token
    http_client = None
    headers = {
        "token": token,
        "instance_id": instance_id
    }
    pass

@app.route('/v2/service_instances/<instance_id>/last_operation')
def get_last_operation(instance_id):
    global token
    http_client = None
    headers = {
        "token": token,
        "instance_id": instance_id
    }
    pass