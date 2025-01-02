'''
Write a Python program that continuously prompts the user 
to input a fruit name. If the input is "apple," the program 
should print "You got it!" and stop. Otherwise, it should 
display "Try again" and continue.
'''

while True:
    userinput=input("Enter a type of fruit: ")

    if userinput!='apple':
        print("Try again")
    
    elif userinput=='apple':
        print("You got it!")
        break