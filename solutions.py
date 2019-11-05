# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

# easiest approach using slicing
def reverse_string(string):
    return string[::-1]

# with for loop
def reverse_string(string):
    result = ''
    for c in string:
        result = c + result  # concatenate from left is important
    return result

# using recursion
def reverse_string(string):
    return string if len(string) in (0, 1) else reverse_string(string[1:]) + string[0]

def reverse_string(string):
    return ''.join(reversed(string))


def is_palyndrom(string) -> True:
    return string == reverse_string(string)

# 1. Write a function to calculate the inner product between two vectors.
x = [1, 2, 3]
y = [4, 5, 6]

def inner(x, y):
    acc = 0
    for i in range(len(x)):
        acc += x[i]*y[i]
    return acc

def inner(x, y):
    return sum([xi * yi for (xi, yi) in zip(x, y)])

def inner(x, y):
    import numpy as np
    return np.dot(x, y)


# How can we calculate how many capital letters are in a string?
test = 'testStrinG'


def count_capital_letters(string):
    cnt = 0
    for letter in string:
        if letter.isupper():  # or letter == letter.upper()
            cnt += 1
    print('There are {0} capital letters'.format(cnt))
    return cnt


def count_capital_letters(string):
    return sum([1 for c in string if c.isupper()])


#  Given a value and a list of coefficients, evaluate the polynomial determined by such coefficients.
def poly(x, coeffs):
    val = 0
    for i, coeff in enumerate(coeffs):
        val += coeff*x**i
    return val


def distance_between_two_vectors(x: list, y: list):
    result = 0
    for i in range(len(x)):
        result += (x[i] - y[i])**2
    return result**0.5


def distance_between_two_vectors(x: list, y: list):
    return sum([(x[i] - y[i])**2 for i in range(len(x))])**0.5


# numpy library hast this implemented
def distance_between_two_vectors(x: list, y: list):
    import numpy as np
    x = np.array(x)
    y = np.array(y)
    return np.linalg.norm(x - y)


def is_number(string):
    for c in string:
        if not '0' <= c <= '9':
            return False
    return True
            
    
def is_letter(string):
    return len(string) == 1 and 'a' <= string.lower() <= 'z'
    
def is_prime_number(n):
    if n in (0, 1):
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True
    
def prime_numbers_under(n):
    prime_numbers = []
    for number in range(2, n):
        if is_prime_number(number):
            prime_numbers.append(number)
    return prime_numbers
        
    
# for i in prime_numbers():
#    do_something(i)
