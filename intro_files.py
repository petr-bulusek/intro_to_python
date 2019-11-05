# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

f = open('path/to/file', mode='r/w/a', encoding='utf-8')

# do something

f.close()


# better is 
with open(...) as f:
    # do things
    content = f.read()
    
    
line = f.readline()

for line in f:
    print(line)
    
with open(...) as f:
    f.write(content)

# automatically closes file even if errors occur
    


# dictionaries
# json
# format used very much for data interchange on the web, API's ...
import json

d = {'key': 'value'}

with open('out.json', 'w') as f:
    json.dump(d, f)

with open('out.json') as f:
    d2 = json.load(f)
