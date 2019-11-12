# -*- coding: utf-8 -*-
"""
@author: pablo maldonado, petr bulusek
"""

# BeautifulSoup docs:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup

# Scrapping Prague's wikipedia
res = requests.get('https://httpbin.org/html')

res.status_code # Status: 200 is ok, 404 is not found

soup = BeautifulSoup(res.text)
# soup = BeautifulSoup(res.text, "lxml")  # second parameter is used parser

# Print the page to see that format is correct
soup

soup.html
p = soup.html.body.div.p
type(p.string)
p.string.parent.parent


p = soup.find('p')
p_list = soup.find_all('p')

.find_next
.find_next_siblings
...
# optional arguments:
# id=
# class_=
# attrs= {'id': 'id_value'}
# tex=

.select(css_selector)


res = requests.get('https://en.wikipedia.org/wiki/Prague')
soup = BeautifulSoup(res.text)

soup.find('span', id='Public_universities')
unis = soup.select('#Public_universities')[0].find_next('ul').find_all('li')
                   
for uni in unis:
    print(uni.text)



# Hospodarske noviny: top 10

res = requests.get('http://ihned.cz')

page = BeautifulSoup(res.text) 


# Get all links
for link in page.find_all('a'):
    print(link.get('href'))


# Titles of first page articles
headlines = page.find_all("div", class_="stats-article ga-edl ga-edl-most_read")

type(headlines) #It's a list! so we can iterate
len(headlines)


for h in headlines:
    print('*'*10)
    print(h.find('a')['href']), print(h.text)


# Parse it for something else
urls = ['http:'+h.find('a')['href'] for h in headlines]
urls
desc = [h.find('a').text for h in headlines]
   

# Remove those cute hats
#import unidecode
#unidecode.unidecode(desc[0])


# Save the data
with open('demo.csv','w', encoding='utf8') as f:
    for h in zip(urls,desc):
        f.write(h[0]+';'+h[1]+'\n')    


### EXERCISE: Can you modify the code to save the urls without diacritics?
## how about including the authors too?
authors = [h.find('a')['data-author'] for h in headlines]


##################################################################
## EXERCISE: Parsing that horrible Cinemacity website
##################################################################
res = requests.get("http://cinemacity.cz/scheduleInfo?locationId=1010105&date=null&venueTypeId=0&hideSite=0&openedFromPopup=1")
page = bs4.BeautifulSoup(res.text, "lxml")

movies_table = page.find('table', {'class':"scheduleInfoTable"})
movies_tbody = movies_table.find('tbody')

rows = movies_tbody.find_all('tr')

with codecs.open('movies.csv', 'w',encoding='utf8') as f:
    for row in rows:
        cols = row.find_all('td')
        row = [el.text.strip() for el in cols]
        title = row[0]
        clasif = row[1]
        audio = row[2]
        text = row[3]
        duration = row[4]
        times = [t for t in row[5:] if t != '']
        f.write(title + '|'+clasif+'|'+audio+'|'+text+'|'+duration+'|'+str(times)+'\n')