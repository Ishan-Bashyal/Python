#Write a Python program to check if a given character is uppercase, lowercase, or a digit. python

char = input("Enter a character: ")
if char.isdigit():
    print(f'{char} is a Digit.')
elif char.isupper():
    print(f'{char} is in Upper Case.')
elif char.islower():
    print(f'{char} is in Lower Case.')