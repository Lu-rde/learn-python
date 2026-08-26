# Dayt 3: Operators & Expressions

# Today I´m learning about different types of operators in Python

#Aritmetic Operators
print("Aritmetic Operators:")
print ("10+2=", 10 + 2) 
print ("10//3 =", 10//3) #this calculates the divission
print ("10 %3 = " , 10%3) # this gives you the decimals of the division
print ("10 ** 2 =", 10 **2)
"""
Here we learn that operations mustnt go between commas 
if you want to see the end result, if you want to print the operation th e
do put it in commas 
"""

# Assingment operators
print ("Assingment Operators: ")
x=5
y=3
print("x=",x,"y=",y)
print ("x*y=",x*y)

"""
Here we learn that you can assign different values to variables 
and oparate with tha varaibles instead of with numbers
"""

# Comparison Operators
a=10
b=20
print ("a==b",a==b)
print("a != b:", a != b)  
print("a > b:", a > b)    
print("a < b:", a < b)    
print("a >= b:", a >= b)  
print("a <= b:", a <= b) 

"""
 Here we learn that if we put just one = we are asingnnin a value
 to a variable,if we put two == we are asking or  checking if two 
 numbers or variables are the same.
 It is going to print out a TRUE/FALSE result !!!
"""

#Logical Operators 
print ("\n Logical OPerators :")

"""
the \n actually spces it out, it pushes it one space away from the 
margin.
"""

is_sunny = True
is_weekend= False
print ("is_sunny and is_weekend", is_sunny and is_weekend)
print ("is_sunny or is_weekend", is_sunny or is_weekend)
print ("not is_sunny:", not is_sunny)

"""
It basically confirms if two or more variables are given at the same time 
or it hands out the oposite of a given variable.
"""

#Identity & Membership Operators 
print ("\n Identity Operators" )

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print ("a is b:", a is b)
print ("a is c:", a is c)
print ("a == c:", a == c)

print ("\n Membership Operators:")
print("2 in [1, 2, 3]:", 2 in [1, 2, 3])
print("4 not in [1, 2, 3]:", 4 not in [1, 2, 3])

"""
This way you compare variables with more than one value associated with it
and you can check if a speciifc value is inside a variables´s values.
"""