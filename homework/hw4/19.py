#Write a program to find the largest number in a list: [3, 7, 2, 8, 5].

list = []
num = int(input("How many number would you add: "))
for i in range(num):
    new_num = int(input(f"Enter {i+1} number: "))
    list.append(new_num)

largest_num = 0
for i in list:
    if i > largest_num:
        largest_num = i

print(f"The largest number is: {largest_num}")