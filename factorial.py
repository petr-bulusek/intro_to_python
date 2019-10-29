# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:41:35 2019

@author: petr bulusek
"""

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result


# with recursion
#def factorial(n):
#    if n == 0 or n == 1:
#        return 1
#    return n * factorial(n-1)
#
#
## one line
#def factorial(n):
#    return 1 if n in (0, 1) else n * factorial(n-1)

factorial(5)