# Day 1: Variables and Data Types

"""
Today I explored how variables work in python and surprisingly enough,
you dont have to define the type. So tehy are quite simple.
"""

#String
name= "Lucía"
language = "spanish"
print (name,language)

#INteger and Float
age = 17
height = 1.68
print (age, height)

#Boolean
learning = True
is_cool= False
print (learning,is_cool)
#NoneType
middle_name=None 
print (middle_name)

"""
type() tells you the function type
"""
print (type(name))

#int to float 

x=5
y=float(x)
print (y,type(y))

#number to string 

number=100
text = str(number)
print (text, type(text))

# string to int
 
x="5"
y= int (x)
print (y, type(y))

"""
if you try to convert a non numerical variable to an int
python will throw an error :)
"""
"""
RECAP:

YOu have different types of variables and you can convert them into 
what you preffer (except for letters to numbers)

We have 
String --> str (letters or sentences and you have to put them between "")
Int -----> int (whole numbers)
float ---> float (decimals)
Boolean -> True / False
None ----> None 

¡¡¡¡CAPITAL LETTERS ARE IMPORTANT!!!!
"""
