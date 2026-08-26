# Day 4: Conditional Statements 

# SImple Statement 
print ("\n Simple Statement:")
x=10
if x>5:
    print ("x is greater than 5")

"""
Here I learn that when something is conditioned by another thing or it belongs
in a specific place it moves a space.
"""

#if-else Statement
print ("\n if-else Statement:")
age =17
if age>=18:
    print ("You are an adult")

else :
    print ("You are a child")


"""
Here I learnt that it is very important to finish a satement with : if you want it
to work
"""

# if-elif-else Ladder
print ("\n if-elif-else Ladder:")
marks =75
if marks >= 90:
    print (marks,", Grade :A")
elif marks>=75:
    print (marks,", Grade :B")
elif marks >=60:
    print ("Grade :C")
else :
    print ("Grade :D")

# Nested if
print ("\n Nested if:")
num=15
if num>0:
    if num % 2 == 0:
        print ("Positive Even Number")
    else: 
        print ("Positive odd number")
else : 
    print ("Negative Number")

"""
You can add conditions to conditios creating a sort of nest.
"""

#Boolean Variables in Conditions 
print ("\ Boolean Variables in Conditons:")

is_logged_in = True 
if is_logged_in:
    print ("Welcome back!")
else: 
    print ("Please log in.")

#Short-Hand if and if-else
print ("\n Short Hand:")

x=5
y=10
if x<y: print ("x is less than y") #One-line if

#One line if-else
print ("Even" if x% 2 == 0 else "Odd")