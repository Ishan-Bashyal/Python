'''
Write a Python program to check if a person is eligible to watch a movie based on their age:
Age >= 18: Allowed
Age < 18: Not Allowed
'''

age = int(input("Enter your age"))
if(age>=18):
    print("Allowed")
else:
    print("Not Allowed")