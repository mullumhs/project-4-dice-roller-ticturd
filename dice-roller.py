"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: dice-roller.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random

#user input function
def get_number(prompt):
    while True:
        try:
            userint = int(input(prompt))
            return userint
        
        except:
            print("Please enter a valid number")


#amount of dice function
def dice_amount():
    userdiceamount = get_number("Please enter the amount of dice you want to roll:")
    return userdiceamount

#amount of dice sides function
def dice_sides():
    userdicesides = get_number("Please enter the amount of sides you want on your dice:")
    return userdicesides






