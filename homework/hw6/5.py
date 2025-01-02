'''
Write a Python program that keeps asking the user to enter a 
day of the week. If the input is not "Sunday," print "It's not 
the weekend yet." The loop should break and print "Enjoy your weekend!"
 when the input is "Sunday."
'''

while True:
    userinput=input("Enter a day of the week: ").title()

    if userinput!='Sunday':
        print("Wrong password, try again")
    
    elif userinput=='Sunday':
        print("Enjoy your weekend!")
        break