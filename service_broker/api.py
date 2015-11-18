from flask import Flask
##############

app = Flask('service-broker')

token = None

@app.route('/v2/catalog')
def list_services():
    global token
    username = 'admin'
    password = 'dangerous'

    pass

@app.route('/v2/service_instances/<instance_id>', methods=['PUT'])
def provision_instance():
    global token

    pass

@app.route('/v2/service_instances/<instance_id>', methods=['PATCH'])
def update_instance():
    global token

    pass

@app.route('/v2/service_instances/<instance_id>/service_bindings/<binding_id>', methods=['PUT'])
def bind_instance():
    global token

    pass

@app.route('/v2/service_instances/<instance_id>/service_bindings/<binding_id>', methods=['DELETE'])
def unbind_instance():
    global token

    pass

@app.route('/v2/service_instances/<instance_id>', methods=['DELETE'])
def deprovision_instance():
    global token

    pass

@app.route('/v2/service_instances/<instance_id>/last_operation')
def get_last_operation():
    global token

    pass