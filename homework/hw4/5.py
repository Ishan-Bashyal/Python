'''
Write a program to print the following using forloop
a. first 10 even numbers
b.first 10 odd numbers
'''
odd=[]
even=[]
for i in range(1,11):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
