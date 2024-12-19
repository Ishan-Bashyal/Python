'''
Write a program to whether a number (accepted from user) is divisible by 2
and 3 both.
'''

number = int(input("Enter a number: "))

if number % 2 == 0 and number % 3 == 0:
    print("It is divisible by both 2 and 3.")
else:
    print("It is not divisible by both 2 and 3.")