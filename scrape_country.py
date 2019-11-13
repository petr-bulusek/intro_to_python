# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:51:31 2019

@author: petr bulusek
"""

res = requests.get('https://en.wikipedia.org/wiki/Prague')
soup = BeautifulSoup(res.text)

b = soup.find('b', text='Foreign residents in the city (2018)')
table = b.parent.parent.parent.parent

trs = table.find_all('tr')

