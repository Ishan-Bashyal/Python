'''
Write a program to accept two numbers and mathematical operators and
perform operation accordingly.
Like:
Enter First Number: 7
Enter Second Number : 9
Enter operator : +
Your Answer is : 16
'''

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
    print(f"Your Answer is: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Your Answer is: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Your Answer is: {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Your Answer is: {result}")
    else:
        print("Division by zero is Invalid.")
else:
    print("Invalid operator!")