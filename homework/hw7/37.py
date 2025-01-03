#Python program to count the number of even and odd numbers from a series of numbers.  

num = []
even = 0
odd = 0

size = int(input("Size of list: "))

i = 0
while i < size:
    new_num = int(input(f"Enter {i+1} Number: "))
    num.append(new_num)
    i += 1

j = 0
while j < len(num):
    if num[j] % 2 == 0:
        even += 1
    else:
        odd += 1
    j += 1

print(f"Number of even numbers: {even} and odd numbers: {odd}")
