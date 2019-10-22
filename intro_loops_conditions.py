# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

# repeating n-times
# function range and for loop

n = 10

for variable_name in range(1, 10, 2): # variable gets values 0, ..., n-1
    print(variable_name)
    print("statement1")
    print("statement2")
    print("statement3") # block of statements
print("this statement is executed after the for loop")


# range arguments
range(10)
range(1, 10, 2)

range(start, stop, step)


# if condition
number = 2
if number % 2 == 0:
    print(number, 'is even number')

    
# if, else condition
number = 2
if number % 2 == 0:
    print(number, 'is even number')
else:  # optional
    print(number, 'is odd number')
    

points = 99
    
if points > 90:
    print('You get the grade A')
else:
    if points > 80:
        print('You get the grade B')
    else:
        if points > 70:
            print('You get the grade C')
        else:
            print('You failed')


# elif
if points > 90:
    print('You get the grade A')
elif points > 80:
    print('You get the grade B')
elif points > 70:
    print('You get the grade C')
else:
    print('You failed')


# Python does not have switch - case


# while loop, wen don't the how many times in advance
i = 0
while i < 10:
    print(i)
    i += 1

# break
# continue   
    
i = 0
while True:
    print(i)
    i += 1
    if i > 10:
        break
    

# continue, skip the rest and continue with next value
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    


# correct user input