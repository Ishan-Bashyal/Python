'''
Take an employee's monthly salary as input. If it's more than 50,000, classify as "High Earner". 
If less than or equal to 50,000, check if it's more than 20,000 to classify as "Mid Earner", 
else classify as "Low Earner".
'''

salary = float(input("Enter the employee's monthly salary: "))

if salary > 50000:
    print("High Earner")
elif salary > 20000:
    print("Mid Earner")
else:
    print("Low Earner")