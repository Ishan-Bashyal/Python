'''
N students take K apples and distribute them among each other evenly. The
remaining (the indivisible) part remains in the basket. How many apples will
each single student get? How many apples will remain in the basket? The
program reads the numbers N and K. It should print the two answers for the
questions above.
'''

N = int(input("Enter the number of Students: "))
K = int(input("Enter the number of Apples: "))
if N > K:
    print("Not enough apple for everyone")
else:
    apple = K // N
    basket = K - apple * N
    print(f"{N} students will get {apple} apples and {basket} apples will be in the basket.")


