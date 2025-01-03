#program to check given number is palindrome or not

num = input("Enter a number: ")
reverse = ''

for i in range(len(num)-1,-1,-1):
    reverse += num[i]

if num == reverse:
    print(f"{num} is Palindrome.")
else:
    print(f"{num} is not a Palindrome number.")