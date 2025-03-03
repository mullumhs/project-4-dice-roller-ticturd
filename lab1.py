"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random

# Write a function named welcome_message that prints out "Welcome to our program!" whenever it is called.
def welcome_message():
    print("Welcome to our program!")

# Create a function named print_divider that prints out a line of asterisks (e.g., "**********") to act as a section divider.
def print_divider():
    print("*************")

# Write a function named get_number that asks the user to input a whole number and then returns the result as an integer.
def get_number():
    a = int(input("Please enter an integer:"))
    return a

# Create a function named get_random_colour that, when called, returns a random colour from a predefined list of colours.
def get_random_colour():
    randomcolor = random.randint(1, 3)

    if randomcolor == 1:
        return "Red"


    if randomcolor == 2:
        return "Blue"
    
    if randomcolor == 3:
        return "Green"
    
# Call all of your functions to demonstrate that they work
welcome_message()
print_divider()
print(get_number())
print(get_random_colour())