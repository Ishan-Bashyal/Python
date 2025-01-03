#factorial of a given number

num = int(input("Enter a number: "))
fact = 1
i=1
while i<num+1:
    fact *= i
    i+=1
print(f"The factorial of {num} is {fact}")