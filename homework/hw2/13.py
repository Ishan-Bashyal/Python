'''
A company decided to give bonus of 5% to employee if his/her year of
service is more than 5years. Ask user for their salary and year of service
and print the net bonus amount.
'''

timeperiod = int(input("Enter year of service: "))
salary = int(input("Enter your salary: "))

if timeperiod > 5:
    bonus = salary * 0.05
    print(f"Your bonus is Rs.{bonus}")
else:
    print("No bonus.")
