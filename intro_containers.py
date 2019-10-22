# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

# back to strings
# string can be seen as list (container) of characters
s = "Python"
s[0]
s[0] = 'C'

# methods
# split
# join

# mutable/immutable types

# slicing
s = "Hello World"
len(s)
s[1:11]
s[1:]
s[0:5]
s[:5]
s[:5:2]
s[-1]
s[-2:-6:-1]

# reverse string?
# reverse string without slicing

# methods
# replace
# upper
# lower
# strip
# rstrip
# lstrip
# split

for c in "Python":
    print(c)
    
count = 0
string = "Python"
for c in string:
    count += 1

# list
l = [1, 2, 3]
l = list()
l.append(1)
l.append(2)
l.append(3)
a = l.pop()

l2 = l
l.append(3)

# making copy with list()


numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)

names = ['Petr', 'Pavel', 'John', 'Jane', 'Lucy']
for name in names:
    print(name)

for i, name in enumerate(names):
    print(i, name)

# list comprehension


# tuple (immutable)
t = (1, 2, 3)
t = (1, 'string', [1, 2])
t = 1, 2, 3


# dict
d = {}
d = dict()

value = 1
d['key'] = value
# keys should be immutable type
# get value
d['key']
d.get('key')

phonebook = {}
phonebook['Petr'] = '123456789'
phonebook['John'] = '777111222'

personal_data = {}
personal_data['name'] = 'Monty Python'
personal_data['email'] = 'monty@python.org'
personal_data['age'] = 42

d = dict(a=1, b=2)

# loop over keys
for k in d:
    print(k)

# loop over values
for v in d.values():
    print(v)

# loop over key, value pairs
for k, v in d.items():
    print(k, ':', v)


# set
s = set()
s.add(1)
s.add(2)
s.add(1)
