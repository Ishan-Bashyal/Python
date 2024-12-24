'''
Write a Python program to print the even numbers from a given list. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

list = []
num = int(input("How many number would you add: "))
for i in range(num):
    new_num = int(input(f"Enter {i+1} number: "))
    list.append(new_num)

for i in list:
    if i % 2 != 0:
        print(i)