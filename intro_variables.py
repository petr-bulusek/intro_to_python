# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

# variables
a = 1
b = 2
c = a + b

# id

b = a

# a is x # compares objects
# == compares values

# good naming is key
# conventions variable_name


# input from user
name = input("Tell me your name please: ")
print("Hi", name)
print("Have a nice day.")


# convert euros to czech crowns
amount_euros = input("Tell me how much euros you have: ")
if amount_euros:
    crowns = int(amount_euros) * 25
    print("You have", crowns, "crowns")
else:
    print("Please tell me")


# more operators
a = 0
a = a + 1
a += 1  # the same but shorter

# del variable
