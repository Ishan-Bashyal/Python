#Python program to calculate the sum of all the even numbers within the given range.

rangee = int(input("Enter a number: "))
sum_even = 0
i = 1 

while i <= rangee:
    if i % 2 == 0: 
        sum_even += i
    i += 1 

print("The sum of odd numbers is:", sum_even)