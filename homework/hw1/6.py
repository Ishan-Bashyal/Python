'''Write a program to accept two numbers and mathematical operators and perform operation accordingly.
Like:
Enter First Number: 7
Enter Second Number : 9
Enter operator : +
Your Answer is : 16'''

numa = float(input("Enter first number: "))
numb = float(input("Enter second number: "))
op = input("Enter operator: ")
if(op== '+'):
    print(f"Your answer is: {numa + numb}")
elif(op== '-'):
    print(numa - numb)
elif(op== '*'):
    print(f"Your answer is: {numa * numb}")
elif(op== '/'):
    print(f"Your answer is: {numa / numb}")
elif(op== '%'):
    print(f"Your answer is {numa % numb}")
elif(op== '**'):
    print(f"Your answer is {numa ** numb}")
elif(op== '//'):
    print(f"Your answer is {numa // numb}")