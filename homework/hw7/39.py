#Write a for loop to find the sum of even and odd numbers separately in a range from 1 to 100.

oddsum = 0
evensum = 0
for i in range(1,100):
    if i % 2 == 0:
        evensum +=i
    elif i % 2 != 0:
        oddsum += i
print(f"Even sum is: {evensum}")
print(f"Odd sum is: {oddsum}")