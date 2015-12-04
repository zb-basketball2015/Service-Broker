__author__ = 'zhaob8'

import json
import logging
import requests
from service_broker.config import DEFAULT_VALUES, body

logger = logging.getLogger(__name__)

username = body['user']['username']
password = body['user']['password']
host = DEFAULT_VALUES['api_host']
port = DEFAULT_VALUES['api_port']

def do_request(action, url, pay_load, headers, files):
    if action == "get":
        return __do_get(url)
    elif action == "post":
        return __do_post(url, pay_load, headers, files)
    elif action == "delete":
        return __do_delete(url)
    elif action == "put":
        return __do_put(url, pay_load, headers, files)
    else:
        error_info = "Action is not acceptable."
        logger.error(error_info)
        return "{'error':%s}" % error_info

def __do_post(url, payload, headers, files):
    logger.debug("URL: %s" % url)
    logger.debug("payload: %s" % json.dumps(payload))
    logger.debug("headers: %s" % json.dumps(headers))
    r = requests.post(url, data=payload, headers=headers, files=files)
    logger.debug("Return: %s" % r.text)
    return __to_json(r.text), r.status_code

def __do_get(url):
    logger.debug("URL: %s" % url)
    r = requests.get(url)
    logger.debug("Return: %s" % r.text)
    return __to_json(r.text), r.status_code

def __do_delete(url):
    logger.debug("URL: %s" % url)
    r = requests.delete(url)
    logger.debug("Return: %s" % r.text)
    return __to_json(r.text), r.status_code

def __do_put(url, payload, headers, files):
    logger.debug("URL: %s" % url)
    logger.debug("payload: %s" % json.dumps(payload))
    logger.debug("headers: %s" % json.dumps(headers))
    r = requests.put(url, data=payload, headers=headers, files=files)
    logger.debug("Return: %s" % r.text)
    return __to_json(r.text), r.status_code

def __to_json(text):
    try:
        return json.loads(text)
    except ValueError:
        logger.debug("Cannot translate to JSON: %s" % text)
        return text