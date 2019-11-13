# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

import requests
from datetime import datetime
import pytz
import json
import os
from dictdiffer import diff


old_estates = {}

if os.path.exists('data.json'):
    with open('data.json', 'r') as fp:
        old_estates = json.load(fp)

new_estates = {}
price_limit = 7000000  # czk
distance = 10  # km
time_now = datetime.utcnow()
time_now = time_now.replace(tzinfo=pytz.utc)
cet_tz = pytz.timezone('Europe/Prague')

# you can find this api url in the developer tools
# tab network
# when viewing the real estates listing page
api_url = "https://www.sreality.cz/api"
url = api_url + "/cs/v2/estates" \
      "?category_main_cb=2&" \
      "category_type_cb=1&" \
      "distance={distance}&" \
      "per_page=200&" \
      "region=obec+Rokytnice+nad+Jizerou&" \  # replace to own town of interest, check from url
      "region_entity_id=2739&" \
      "region_entity_type=municipality".format(distance=distance)

response = requests.get(url)
j = response.json()
estates = j['_embedded']['estates']

for estate in estates:
    data = {}
    estate_url = api_url + estate['_links']['self']['href']
    hash_id = estate['hash_id']
    price = estate['price']
    data['price'] = price
    res = requests.get(estate_url)  # get further info from ecah estate url
    estate_j = res.json()
    estate['detail'] = estate_j
    locality = estate_j['seo']['locality']

    if price < price_limit:
        estate_detail_url = "https://www.sreality.cz/detail/prodej/dum/rodinny/" + locality + '/' + str(hash_id)
        new_estates[estate_detail_url] = data

# check what changed since last scrape
result = diff(old_estates, new_estates)
res_list = list(result)
print(res_list)

# save new scraped data
with open('data.json', 'w') as fp:
    json.dump(new_estates, fp)

