# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

# object oriented programming

# 1 encapsulation
# 2 inheritance
# 3 polymorfism

# object: container with some data and methods (functionality around that data)
# a class defines how these objects look like and behave
# we have seen already how to call these methods on strings, lists, ...


class Cat:
    pass


# __init__
    
# methods (functions indented under class, first parameter is 'self')


#class Cat:
#    def greet(self):
#        print("Miau")


# subclassing
class Animal:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print('I am an animal')


class Cat(Animal):
    def greet(self):
        print('Miau')


class Dog(Animal):
    def greet(self):
        print('Woof')


animals = [Animal('Bob'), Cat('Pusheen'), Dog('Aron')]

for animal in animals:
    print("Hi, i am", animal.name, "and saying: ", end='')
    animal.greet()
