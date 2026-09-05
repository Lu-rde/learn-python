# Day 12: Modules & Packages

"""
Today I learned how python modules and packages work.
This helps in code and reusing functions across different files.
"""

# ---Built-in Modules

import math
import random
import datetime

print ("Square root of 16:", math.sqrt(16))
print ("Random number between 1 and 10:", random.randint(1,10))
print ("Current date and time:", datetime.datetime.now())

"""
Python comes with many built-in modules like math, random, datetime, os sys, etc.
I use rando in the day 10 mini project I built.
"""

# ---Creating a custom Module---

"""
I'll try creating my first own module.
I'll create a separate file called 'my utils.py' (in the same folder)
Making my own module isn't that difficult. Basically, you define some functions in that
file and then import then directly in your own code.
"""

# CONTENTS OF my_utils.py (Create this file separately!)
# def greet(name):
#     return f"Hello, {name}!"

# def add(a, b):
#     return a + b

# Now using my custom module here

import my_utils # make sure the file exists in the same folder

print (my_utils.greet("Lucía"))
print ("3+7=", my_utils.add(3,7))

# --- Creating a Package ---

# For now, I didn't go deep into creating packages, but these basics helped me understand how larger projects are organized.