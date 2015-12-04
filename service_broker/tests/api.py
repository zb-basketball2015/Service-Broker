from flask import Flask
##############

app = Flask('service-broker')

@app.route('/v2/catalog')
def list_services():

    pass

@app.route('/v2/service_instances/<instance_id>', methods=['PUT'])
def provision_instance():

    pass

@app.route('/v2/service_instances/<instance_id>', methods=['PATCH'])
def update_instance():

    pass

@app.route('/v2/service_instances/<instance_id>/service_bindings/<binding_id>', methods=['PUT'])
def bind_instance():

    pass

@app.route('/v2/service_instances/<instance_id>/service_bindings/<binding_id>', methods=['DELETE'])
def unbind_instance():

    pass

@app.route('/v2/service_instances/<instance_id>', methods=['DELETE'])
def deprovision_instance():

    pass

@app.route('/v2/service_instances/<instance_id>/last_operation')
def get_last_operation():

    pass