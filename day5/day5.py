# Day 5: Loops & Iteration

# The white loop
print ("\n while Loop:")
count = 1
while count <= 5:
    print ("Count is:", count)
    count += 1

"""
Here we learn that you can add multiple steps to asingle loop.
And the loop will stop once the condition you state does no longer
correspond.
"""

# Infinite Loop (be careful!)
"""
while True:
print (This will run forever unless there´s a break)
"""

# Using break and continue 
print ("\n Using break and continue " )
i=0
while i < 10:
    i+= 1
    if i == 5 :
        continue # Skips 5
    if i == 8:
        break # Stops the loop when i is 8
    print (i)

# The for loop (Much cleaner!)
print ("\n The for loop with range ():")
for num in range (1,6):
    print ("Number:", num)

# range (start,stop,step)
print ("\n Loop with step:")
for num in range (0,10,2):
    print (num)

"""
This is very important for it allows you to create more complex 
loops.
"""

#Looping through a List
print ("\n Looping through a List:")
colors = ["red", "green", "blue"]
for color in colors :
    print ("Color:", color )

# Looping through a String
print ("Looping through a String:")
word = "Python"
for char in word :
    print (char)

"""
Here the variables color and char are automatically created by Python
the momemt the fo loop begins.
"""

#Nested Loops
print ("\n Nested Loops:")
for i in range (1,4):
    for j in range (1,3): 
        print (f"i = {i}, j = {j}")

#Using else with loops
print ("\n Using else with loops:")
for n in range (3):
    print ("Number:",n)
else:
    print ("Loop finished!")

"""
Here we see that if we dont add a begginig and end, the number is considered 
the end and it starts with 0.
"""