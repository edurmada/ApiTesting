"""
Auxiliary library for methods used in testcases
"""

import requests
import json
import urllib
from libs.logger import log_request

# Load configuration on import. Scripts run from the root directory.
with open("config.json", "r") as rh:
    CONFIG = json.load(rh)

@log_request
def send_request(url, data, **params):
    """
        Auxiliary method to send Request
    """
    if params['request_type'] == "POST":
        response = requests.post(CONFIG["BASE_URL"] + url + "?" + urllib.parse.urlencode(params),
            data = data)
    elif params['request_type'] == "GET":
        response = requests.get(CONFIG["BASE_URL"] + url + "?" + urllib.parse.urlencode(params))
    else:
        raise ValueError("Request Type is not supported")

    # Format the response into JSON if possible
    if response.headers['Content-Type'] == 'application/json;charset=utf-8':
        return json.loads(response.text)
    return response

def send_get_request(url, **params):
    """
        Auxiliary method to load API TOKEN together with uri params to symplify testcase syntax
    """
    params['api_key']= CONFIG["TOKEN"]
    params['request_type']= "GET"
    if "data" in params.keys():
        return send_request(url, **params)
    else:
        return send_request(url, data="", **params)

def send_post_request(url, data, **params):
    """
        Auxiliary method to load API TOKEN together with uri params to symplify testcase syntax
    """
    params['api_key']= CONFIG["TOKEN"]
    params['request_type']= "POST"
    return send_request(url, data, **params)