'''
Write a Python program to sum all the numbers in a list using for loop.
Sample list : [8, 2, 3, 0, 7]
'''

list = []
num = int(input("How many number would you add: "))
for i in range(num):
    new_num = int(input(f"Enter {i+1} number: "))
    list.append(new_num)

sum = 0
for i in list:
    sum += i
print(f"Sum of the list {list} is: {sum}")