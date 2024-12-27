#Python program to calculate the sum of all the odd numbers within the given range.

rangee = int(input("Enter a number: "))
sum_odd = 0
for i in range(rangee+1):
    if i % 2 != 0:
        sum_odd += i
print("The sum of even numbers is: ",sum_odd)