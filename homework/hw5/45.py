#Write a program to determine whether a given number is a prime number.

num=int(input("Enter a number: "))
for i in range(2,num):
    if(num%i==0):
        print("Not prime number")
        break
else:
    print("Prime number")