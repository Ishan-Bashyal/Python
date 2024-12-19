'''
Write a Python program that takes a month number (1–12) and outputs the corresponding season:
12, 1, 2: "Winter"
3, 4, 5: "Spring"
6, 7, 8: "Summer"
9, 10, 11: "Autumn"
'''

month = int(input("Enter the month number (1-12): "))
if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    print("Spring")
elif month == 6 or month == 7 or month == 8:
    print("Summer")
elif month == 9 or month == 10 or month == 11:
    print("Autumn")
else:
    print("Invalid month number")