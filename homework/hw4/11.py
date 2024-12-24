'''
Write a Python program to multiply all the numbers in a list using for loop.
Sample list = [8,2,3,-1,7]
'''

list = []
num = int(input("How many number would you add: "))
for i in range(num):
    new_num = int(input(f"Enter {i+1} number: "))
    list.append(new_num)

mul = 1
for i in list:
    mul *= i
print(f"Multiplication of the list {list} is: {mul}")