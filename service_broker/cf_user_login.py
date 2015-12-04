__author__ = 'zhaob8'

from flask import Flask
from service_broker.http_client import host, port, do_request
##############

app = Flask('service-broker')

@app.route('/v2/login', methods=['POST'])
def login(username, password):

    headers = {
        'username':username,
        'password':password
    }
    url = 'http://' + host + port + ':' + '/login'

    try:
        result, status_code = do_request('post', url, None, headers, None)
    except Exception, e:
        print e
    pass