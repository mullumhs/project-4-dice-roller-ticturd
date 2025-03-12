"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions with parameters in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a function named say_hello that accepts a person's name as a parameter and prints "Hello" followed by the name.
def say_hello(name):
    return (f"Hello {name}")

# Develop a function named triple that takes one number as a parameter and returns the number multiplied by three.
def triple(num):
    return num * 3

# Write a function called add that takes two numbers as parameters and returns their sum. 
def sum(x, y):
    return x + y

# Create a function named draw_line that takes one parameter for the length of the line and prints a straight line of that many hyphens.
def draw_line(amount):
    return ("-" * amount)

# Call your functions, printing out the return result where appropriate
print(say_hello("ward"))


num = 2
print(triple(num))


x = 3
y = 5
print(sum(x, y))


amount = 17
print(draw_line(amount))