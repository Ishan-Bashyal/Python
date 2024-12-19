'''
Accept the age, gender ('M', 'F'), number of days and display the wages
accordingly.
Age Gender Wage/day

>=18 and <30 
M 700
F 750

>=30 and <=40 
M 800
F 850
'''



age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days: "))
wage_per_day = 0

if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    elif gender == 'F':
        wage_per_day = 750
elif 30 <= age <= 40:
    if gender == 'M':
        wage_per_day = 800
    elif gender == 'F':
        wage_per_day = 850
else:
    print("Age not within valid range for wages.")


total_wages = wage_per_day * days
print("Wage per day:", wage_per_day)
print("Total wages for", days, "days:", total_wages)
