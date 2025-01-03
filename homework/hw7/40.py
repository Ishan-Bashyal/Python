#program to check given number is palindrome or not

num = input("Enter a number: ")
reverse = ''
i = len(num) - 1

while i >= 0:
    reverse += num[i]
    i -= 1

if num == reverse:
    print(f"{num} is Palindrome.")
else:
    print(f"{num} is not a Palindrome number.")
