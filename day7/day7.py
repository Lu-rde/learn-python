# Day 7: Lists & Tuples

# Creating a list
fruits = ["apple", "banana", "cherry"]
print ("My fruits are:", fruits)

# Accessing the list items
print ("First fruit:", fruits[0])
print ("Thirt fruit:", fruits [2])

# Modifying Lists
fruits.append ("mango")  #Adds at the end
fruits.insert (1, "orange") #Ads at a specific index
print ("After adding fruits:", fruits)

"""
Here we learn that the first item is always 0.
"""

# Removing from list
fruits.remove ("banana") #remove by value
popped =fruits.pop () #remove last
print ("After removal:", fruits)
print ("Removed item:", popped)

#Looping through a list
print ("Looping through fruits:")
for fruit in fruits:
    print (fruit)

#LIst lemgth
print ("Number of fruits:", len(fruits))

# Check if Item Exists
if "cherry" in fruits :
    print ("Yes, cherry is in fruits")
else : print ("Cherry not in fruits")

#List Slicing
print ("First two fruits:", fruits [:2])
print ("Last two fruits:", fruits [-2:])

# Clear or Delete List
# fruits.clear()       # Uncomment to empty list
# del fruits           # Uncomment to delete entire list

# List Comprehension
numbers = [1,2,3,4,5]
squared=[num**2 for num in numbers]
print ("Squares:", squared)

# -----------------------------
# Tuples — Immutable Lists
# -----------------------------

# Creating a Tuple
dimensions =(800, 600)
print ("Dimensions", dimensions )

#Accessing Tuple Elements
print ("Width:", dimensions[0])
print ("Height:", dimensions [1])

#Truples are Immutable
# dimensions [0] = 1024 #Error

# Single -item Truple -> needs a comma
single =("one",)
print ("Single-item truple:", single)

#Looping Through a Truple
print ("Looping Through a truple:")
for dim in dimensions:
    print(dim)

'''
Lists:
- Mutable (changeable)
- Created with square brackets []
- Can be modified (add/remove/update items)

Tuples:
- Immutable (unchangeable)
- Created with parentheses ()
- Faster and used when data shouldn't be changed
'''