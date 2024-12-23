'''
Accept age, gender ('M', 'F'), and income and calculate the tax:
Age >= 18 and < 60:
    Male:
        Income > 10,00,000: Tax = 30%
        Income between 5,00,000 and 10,00,000: Tax = 20%
        Income <= 5,00,000: Tax = 10%
    Female:
        Income > 10,00,000: Tax = 25%
        Income between 5,00,000 and 10,00,000: Tax = 15%
        Income <= 5,00,000: Tax = 5%
Age >= 60:
    Male or Female:
        Income > 10,00,000: Tax = 20%
        Income <= 10,00,000: Tax = 10%
'''

age = int(input("Enter your age: "))
gender = input("Enter your gender ('M' for Male, 'F' for Female): ").upper()
income = float(input("Enter your annual income: "))

if age >= 18 and age < 60:
    if gender == 'M':
        if income > 1000000:
            tax = income * 0.30
        elif 500000 <= income <= 1000000:
            tax = income * 0.20
        else:
            tax = income * 0.10
    elif gender == 'F':
        if income > 1000000:
            tax = income * 0.25
        elif 500000 <= income <= 1000000:
            tax = income * 0.15
        else:
            tax = income * 0.05
    else:
        tax = 0
        print("Invalid gender input.")
elif age >= 60:
    if income > 1000000:
        tax = income * 0.20
    else:
        tax = income * 0.10
else:
    tax = 0
    print("No tax applicable for minors.")

if tax > 0:
    print("Tax to be paid:", tax)