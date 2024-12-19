'''For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative
and print ‘zero’ if it is 0'''

num = int(input("Enter an integer: "))
if num < 0:
    print("False")
elif num==0:
    print("0")
else:
    print("True")