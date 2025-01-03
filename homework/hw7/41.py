#program to check given number is armstrong or not

num = input("Enter a number: ")
arm = 0
length = len(num)
i = 0

while i < length:
    arm += int(num[i])**length
    i += 1

if int(num) == arm:
    print(f"{num} is Armstrong Number.")
else:
    print(f"{num} is not an Armstrong number.")
