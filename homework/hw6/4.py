'''
Create a Python program that asks the user to guess the password.
 The program should keep asking until the user enters "open sesame."
 For each incorrect guess, print "Wrong password, try again." 
When the correct password is entered, print "Access granted!"
'''

while True:
    userinput=input("Guess the password: ")

    if userinput!='open sesame':
        print("Wrong password, try again")
    
    elif userinput=='open sesame':
        print("Access granted")
        break