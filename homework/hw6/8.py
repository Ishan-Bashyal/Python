'''
8. Write a Python program that simulates a basic arithmetic quiz. 
Generate two random numbers between 1 and 30 and ask the user to 
provide the result of their multiplication. If the answer is correct, 
print "Correct!" and generate a new question. If the answer is wrong, 
print "Incorrect, try again." Allow the user to stop the quiz when the 
user enters "exit"
'''

import random
while True:
    a=random.randint(1,30)
    b=random.randint(1,30)
    guess=int(input("Enter your guess: "))

    if a*b!=guess:
        print("Inorrect answer")
        guess=input("Do you want to continue: (yes/no)")
        if guess=="yes":
            continue
        else:
            break
        
    elif a*b==guess:
        print("Correct answer")
        guess=input("Do you want to continue: (yes/no)")
        if guess=="yes":
            continue
        else:
            break
        
