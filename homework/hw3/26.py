'''
Accept the age, gender ('M', 'F'), and membership type ('Monthly', 'Yearly'):
Age >= 18 and < 30:
    Male:
        Monthly: Rs50
        Yearly: Rs500
    Female:
        Monthly: Rs45
        Yearly: Rs450
Age >= 30 and <= 50:
    Male or Female:
        Monthly: Rs60
        Yearly: Rs600
Age > 50:
    Male or Female:
        Monthly: Rs40
        Yearly: Rs400
'''

age = int(input("Enter your age: "))
gender = input("Enter your gender ('M' for Male, 'F' for Female): ").upper()
membership_type = input("Enter the membership type ('Monthly' or 'Yearly'): ").capitalize()

if 18 <= age < 30:
    if gender == 'M':
        if membership_type == 'Monthly':
            membership_fee = 50
        else:
            membership_fee = 500
    elif gender == 'F':
        if membership_type == 'Monthly':
            membership_fee = 45
        else:
            membership_fee = 450
else:
    if 30 <= age <= 50:
        if membership_type == 'Monthly':
            membership_fee = 60
        else:
            membership_fee = 600
    else:
        if membership_type == 'Monthly':
            membership_fee = 40
        else:
            membership_fee = 400

print(f"The membership fee is Rs{membership_fee}")
