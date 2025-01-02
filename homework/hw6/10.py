'''
Write a Python program that asks the user to guess a pre-defined secret
 word (e.g., "python"). Provide feedback like "Incorrect, try again" if the 
guess is wrong. When the user guesses correctly, print "Congratulations, you
 guessed the word!" Allow the user to exit the program by typing "quit."
'''

secret='python'
while True:
    userinput=input("Guess the word: ")

    if userinput!='python':
        print("Incorrect, try again")
        choice=input("Do you want to continue: (yes/exit)")
        if choice=="yes":
            continue
        else:
            break
        
    
    elif userinput=='python':
        print("Congratulations, you guessed the word")
        choice=input("Do you want to continue: (yes/exit)")
        if choice=="yes":
            continue
        else:
            break