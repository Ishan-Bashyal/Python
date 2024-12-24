#Write a python program to print a multiplication table of any number using for loop. 

a=int(input('Enter a value'))

for i in a:
    print(a[i],'x',i,'=',i*a)