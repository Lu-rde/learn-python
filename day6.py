# Day 6: Functions & Scope

#Defining a Simple function
def greet():
    print ("Hello World!")

"""
Here we define a function to then reference it in the future
without having to rewrite everything.
"""

#Calling the function 
greet ()

"""
This is how we reference it in the future when we want to use 
it.
"""

#Function with Parameters
def greet_user (name):
    print ("Hi", name )

greet_user ("Ayush")
greet_user ("Python Learner")

"""
Here we see the example that when we define the function, we are 
giving it a variable, and then we say what we want that fucntion to 
do, so when we call it it uses the value we gave it and makes the 
action we defined.
"""

#Function With return value 
def square (number):
    return number * number

result=square (5)
print ("Square of 5 is :", result)

"""
Here we have created a function named square and we have put a variable 
inside it named number, what said function does is multiply the value 
that we asign to the number by itself, so when we call the variable 
inside the function it essentially does what the function says.
"""

#Function with multiple Parameters
def add (x,y):
    return x+y

print ("Result of 3 + 4:", add (3,4))

#Default Parameters
def welcome (name="Guest"):
    print ("Welcome,", name)

welcome ()
welcome ("Lucía")

"""
Here we see that if we do not give a value to the parameter name, its default
value will be Guest, but if we do give it a value this changes.
"""

#Keyword Arguments
def describe_pet (animal, name):
    print (f"{name} is a {animal}.")

describe_pet ("dog", "Pepa")
describe_pet (name ="Pepa", animal ="dog")

"""
We put f"{name} is a {animal}." when we want to add a variable directly into a 
line of text.
"""

# Variable Scope
"""
Scope = where a variable exists in the code.

Local Scope → Inside a function  
Global Scope → Outside all functions
"""

#Example of Local Scope
def show_number():
    num = 42 #local variable
    print ("Inside function:", num)

show_number ()

#Example of global Scope 
language ="Python "

def print_language ():
    print ("I´m learning", language )

print_language ()

#Modifiying Global Variables Inside a Function
count = 0

def increase_count ():
    global count
    count += 1

increase_count() #This cannot be ommited
print ("Count:", count)

"""
If you want the outside variable to cahnge firs ¡t you have to call 
the function that changes it.
"""