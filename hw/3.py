'''Write a program that asks the user for a number in the range of 1 to 12. 
The program should display the corresponding month, where 
1=january, 2=february,3=march,4=april,5=may,6=june,7=july,8=august,9=september,
10=october,11=november,12=december. The program should display an error message
if the user enters a numberthat is outside the range of 1 to 12.'''

a={1:'January',2:"February",3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
b=eval(input("Enter a number: "))
if b in a:
    print(a[b])
else:
    print("Error")

