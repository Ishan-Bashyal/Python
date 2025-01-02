'''write a code to allow user to enter a number if the number is 0 print gud 
if not 0 count the total sum of the numbers user entered'''

userinput=int(input('Enter a number'))
sum=0
while userinput!=0:
    sum=userinput+sum
    userinput=int(input('Enter a number'))
else:
    print(sum)
