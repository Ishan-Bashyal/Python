'''Write a program to accept the cost price of a bike qnd display the road tax
to be paid according to the following criteria:
Cost price(in Rs) Tax
>100000 15%
>50000 and <=100000 10%
<=50000 5%'''

bikecost = int(input("Enter cost of bike: "))
if bikecost <= 50000:
    tax = 5
elif bikecost > 100000:
    tax = 15
else:
    tax = 10

print(f"Tax for bike is{bikecost * (tax/100)}")