# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""


def func_name(a, b):  # parameters are optional
    """return number
    expects two numbers"""
    print("statement1")  # block of statements
    print("statement2")
    print("other statements...")
    result = a + b
    return result  # optional


# type hints
def func_name(a: list) -> int:
    return len(a)


# debugging