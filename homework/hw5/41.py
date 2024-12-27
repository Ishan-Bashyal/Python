#program to check given number is armstrong or not

num = input("Enter a number: ")
arm = 0
for i in range(len(num)):
    arm += int(num[i])**len(num)

if int(num) == arm:
    print("{num} is Armstrong Number.")
else:
    print("{num} is not a Armstrong number.")