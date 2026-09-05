# Day 14: Class & Objects

"""
Classes define the structure and behaviour (data+ functions), and objects are instances of those classes.
"""

class Car: 
    def __init__(self, brand, model, year):
        self.brand= brand
        self.model= model
        self.year=year
        self.engine_on= False

    def start_engine (self):
        if not self.engine_on==False:
            print (f"{self.brand} {self.model}'s engine stopped.")

        else:
            print("Engine is already off.")

    def info(self):
         print(f"{self.brand}, {self.model}, ({self.year})")


# Creating Objects
my_car= Car (input("What is your car?"), input ("What model?"), input ("What year?"))
my_car.info ()
my_car.start_engine()

# Another Example 
class Book: 
    def __init__(self, title, author, pages):
        self.title=title 
        self.author=author
        self.pages=pages

    def book_info(self):
        print (f"Your favorite book is {self.title},  by {self.author}, {self.pages} pages. ")

book = Book (input("What is your favorite book?"), input ("Who is the author ?"), input ("How many pages does it have ?"))

book.book_info ()