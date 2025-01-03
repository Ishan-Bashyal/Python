#program to print the given number is odd or even

num = int(input("Enter a number: "))
while num % 2 == 0:
    print(f"{num} is even")
    break
else:
    print(f"{num} is odd")
    