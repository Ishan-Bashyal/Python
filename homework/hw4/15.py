#Sum : 1 to 10 (or any number) using for loop.

num = int(input('Enter a number: '))
sum = 0

for i in range(num+1):
    sum += i
print(f'The sum of numbers from 1 to {num} is: {sum}')