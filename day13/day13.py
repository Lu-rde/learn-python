# Day 13: Object-Oriented Programming (OOP)

# What is a class?
"""
A class is like a blueprint for creating objects. It defines attributes (variables) and methods (functions).
"""

# Defining a simple class
class Person:
    def __init__ (self,name,age):
        self.name= name # instance variable
        self.age =age

    # Method
    def introduce(self): 
        print (f"Hi, my name is {self.name} and I am  {self.age} years old.")

# Creating objects (instances) of the class 
person1 = Person ("Lucía", 18)
person2= Person ("Alejandra", 19)

# Calling methods on objects
person1.introduce()
person2.introduce()

"""
'self' refers to the instance of the class. It allows us to access variables and methods associated with the current object.
"""

# More concepts : Class vs Instace variables
class Student :
    college = input("What is your college? \n ")

    def __init__ (self, name):
        self.name = name #instance value (unique to each instace)

    def display (self):
        print (f"{self.name} studies at {Student.college}")

s1= Student("Lucía")
s2= Student("Alejandra")

s1.display()
s2.display()