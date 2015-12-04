__author__ = 'zhaob8'

import os
import json
import ConfigParser

DEFAULT_VALUES = {
    'api_host': '10.32.105.149',
    'api_port': '5000',
    'debug': 'True',
    'token_expiration': '3600',
    'auto_register_service': 'False'
}

body = {
    'user': {
        'username': 'admin',
        'password': 'dangerous'
    }
}

CONF = ConfigParser.ConfigParser(DEFAULT_VALUES)

