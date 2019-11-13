# -*- coding: utf-8 -*-
"""
@author: pablo maldonado, petr bulusek
"""

# Scraping steps:
# check if some API exists
# check if some library exists, you are probably not the only one, if it is popular website
# if dynamically created, check calls to backend APIs
# if no other option, try with scraping the html
# if very dynamically oriented with javascript, you will probably need Selenium library
# be carefull with many requests, infinite loops etc.


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



# Hospodarske noviny

res = requests.get('http://ihned.cz')

page = BeautifulSoup(res.text) 

# Get all links
links = page.find_all('a')

for link in links:
    href = link['href']  # access tag atttributes as keys in dictionary
    # href = link.get('href')
    print(href)


# Titles of most read articles
headlines = page.find_all("div", class_="stats-article ga-edl ga-edl-most_read")

type(headlines) #It's a list! so we can iterate
len(headlines)


for h in headlines:
    a = h.find('a')
    print(a['href'], h.text)


# Parse it for something else
urls = ['http:' + h.find('a')['href'] for h in headlines]
urls
desc = [h.find('a').text for h in headlines]
   


# Save the data
with open('out.csv','w', encoding='utf8') as f:
    for h in zip(urls,desc):
        f.write(h[0]+','+h[1]+'\n')    


# EXERCISE:
# how about including the authors too?
authors = [h.find('a')['data-author'] for h in headlines]
