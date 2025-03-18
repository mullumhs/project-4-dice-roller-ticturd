"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: dice-roller.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import random

def fulldiceroller():
    #user input function
    def get_number(prompt):
        while True:
            try:
                userint = int(input(prompt))
                if userint > 0: #ensures number is positive
                    return userint
                else:
                    print("Please enter a positive number.")

            except:
                print("Please enter a valid number") 


    #dice function
    def diceroll(sides, qty):
        
        total = 0
        for roll in range(1, qty):
            rnd = random.randint(1, sides)
            total = total + rnd
            print(rnd)
        print(f"The total is {total}")    





    #gets user inputs
    sides = get_number("Please enter the amount of sides you want on your dice: ")
    qty = get_number("Please enter the amount of dice you want to roll :")


    #calls functions
    diceroll(sides, qty + 1)





