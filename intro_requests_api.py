# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

# rest API: using http requests for getting, updating, ... data
# GET, POST, UPDATE, DELETE methods
# library for http requests

import requests

response = requests.get('https://httpbin.org/html')

response.status_code
response.headers
response.text

# html document
# tree structure


# json is very popular format for api
# structure containing basic types, lists and dicts can be dumped to json string representation

import json

d = {'name': 'John', 'age': 30, 'hobbies': ['sport', 'music']}
json_str = json.dumps(d)
d2 = json.loads(json_str)


res = requests.get('https://httpbin.org/json')
text = res.text
d = json.loads(text)

d = res.json()
