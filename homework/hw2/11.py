'''
.A company decided to give bonus to employee according to following
criteria:
Time period of service Bonus
More than 10 years 10%
>=6 and <=10 8%
Less than 6 years 5%
'''

timeperiod = int(input("How many years you have been in the company: "))
salary = int(input("How much is your salary: "))
if timeperiod > 10:
    print(f"Your bonus is {salary * 0.1}")
elif timeperiod >= 6 and timeperiod <= 10:
    print(f"Your bonus is {salary * 0.08}")
elif timeperiod < 6 and timeperiod >= 0:
    print(f"Your bonus is {salary * 0.05}")
else:
    print("Invalid time period!")
