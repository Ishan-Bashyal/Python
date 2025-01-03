#Write a program to determine whether a given number is a prime number.

num = int(input("Enter a number: "))
i = 2

while i < num:
    if num % i == 0:
        print("Not a prime number")
        break
    i += 1
else:
    print("Prime number")
