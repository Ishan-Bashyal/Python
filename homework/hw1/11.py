'''
Write a Python program to categorize a person’s age:
Age < 13: Child
13 <= Age <= 19: Teenager
Age > 19: Adult
'''

age = int(input("Enter age:"))
if(age < 13):
    print ("Child")
elif(13 <= age <= 19):
    print("Teenager")
elif(age>19):
    print("Adult")