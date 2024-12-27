#Python program to calculate the sum of all the even numbers within the given range.

rangee = int(input("Enter a number: "))
sum_even = 0
for i in range(rangee+1):
    if i % 2 == 0:
        sum_even += i
print(f"The sum of even numbers is: {sum_even}")