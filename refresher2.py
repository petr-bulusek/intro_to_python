# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

# functions
# containers: string, list, tuple, dict
# indexing
# slicing
# iterating


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# squared numbers for until 5

result = []
for i in some_list:
    squared_i = i*i
    if i <= 5:
        result.append(squared_i)


# list comprehension
[i*i for i in some_list if i <= 5]

# dict comprehension
{i: i*i for i in some_list}


# anonymous functions
squared = lambda x: x**2

squared(2)

list(map(lambda x: x**2, some_list))
