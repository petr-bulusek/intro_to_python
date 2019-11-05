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

cat = Cat()
cat.name = 'Pusheen'
cat.age = 10

# we use __init__ function for that, so we can init the object like that
cat = Cat(name='Pusheen', age=10)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
# methods (functions indented under class, first parameter is 'self')


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Miau")


# subclassing, inheritance
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

# polymorfism
animals = [Animal('Bob'), Cat('Pusheen'), Dog('Aron')]

for animal in animals:
    print("Hi, i am", animal.name, "and saying: ", end='')
    animal.greet()
