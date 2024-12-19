'''Write a Python program to input marks and determine the grade based on the following conditions:
90-100: A
80-89: B
70-79: C
Below 70: Fail'''

marks = int(input("Enter marks"))
if(90 <= marks <= 100):
    print("A")
elif(80 <= marks <= 89):
    print("B")
elif(70 <= marks <= 79):
    print("C")
elif(marks < 70):
    print("Fail")