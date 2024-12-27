#Python program to count the number of even and odd numbers from a series of numbers.  

num = []
even=0
odd=0

list = int(input("Size of list: "))
for i in range(list):
    newlist = input(f"Enter {i+1} Number: ")
    num.append(newlist)

for j in num:
    if int(j) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Number of even are:{even} and odd no. are:{odd}")