#Write a for loop to find the sum of all multiples of 3 or 5 below a given number range from 3 to 99.

sum = 0
i = 3

while i < 100:
    if i % 3 == 0 or i % 5 == 0:
        sum += i
    i += 1

print(f"Sum is: {sum}")