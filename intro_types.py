# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

# numerical types
# int (integer)
# 1, 2, -3, ...
# operators:
# +, -, *, //, %, **
1 + 2
2 * 3
5 // 2
5 % 2
2**2
2**8

10_000_000_000


# float (floating point numbers)
# 1.0, 3.14, ...
# operators:
# +, -, *, /, //, %, **
1.5
.1 + .2 + .3 + .4
2.0 * 3

# Hello

# string type
# "Hello World", 'Hello', 'a', ':-)'
# operators:
# +, *

'Hello'
"Hello"

"Hello" + "World"

"Hello" * 10
'a' * 10

#'a' * 'b'

print("Hello World")
#
#print("Hello 'Petr'")
#print("Hello \"Petr\"")

# multiline strings
"""this file has some
examples for introduction
to Python"""

# escaping
# print("Hello\nworld")
# raw string
path = 'C:\\Users\\Pbulusek'
path = r'C:\Users\Pbulusek'


# boolean type
True
False

# result of comparison operators

1 < 2
0 < 1 < 2

# <, >, ==, !=, <=, >=
# not, and, or


# Complex numbers
complex(1, 2)
complex(3, 4)

# complex(1, 2) < complex(3, 4)
# abs(complex(1, 2)) < abs(complex(3, 4))


# determine type
# type("Hello")
# type(1)
# type(1) == int


# type conversion
# int(), float(), str(), bool()
# str(1)
# str(3.14)
int(3.14)
#int("3.14")


# standard library, math
# import math
# dir
# from math import sin
# from math import 


# help

# special value None
# type(None)
# a is None

from math import pi
print('Area of circle with radius', 10, 'equals to', pi*10*10)
