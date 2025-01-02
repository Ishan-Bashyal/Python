'''
Write a Python program that generates a random number 
between 1 and 10 and prompts the user to guess the number. 
The program should provide hints such as "guess higher" or 
"guess lower" based on the user's input. Once the user guesses
the correct number, the program should display the number of 
attempts it took to guess the correct number.
'''

import random
attempt=0
while True:
    a=random.randint(1,10)
    guess=int(input("Enter your guess: "))
    attempt+=1

    if a!=guess:
        if guess>=a:
            print("Guess lower")
        elif guess<=a:
            print("Guess higher")

    elif a==guess:
        print(f"It took you {attempt} attempts to guess the correct number ")