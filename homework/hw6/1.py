'''
Create a Python program that prompts the user to enter their age. 
If the age is less than 18, print "You are a minor." If the age is 
between 18 and 60, print "You are an adult." For ages over 60, print 
"You are a senior citizen." The program should continue until the user 
inputs "stop."
'''


while True:
    age=int(input('Enter your age'))

    if age<18:
        print("You are a minor")
        choice=input("Do you want to continue: (yes/no)")
        if choice=="yes":
            continue
        else:
            break

    elif age>=18 or age<=60:
        print("You are a adult")
        choice=input("Do you want to continue: (yes/no)")
        if choice=="yes":
            continue
        else:
            break

    elif age>60:
        print("You are a senior citizen")
        choice=input("Do you want to continue: (yes/no)")
        if choice=="yes":
            continue
        else:
            break