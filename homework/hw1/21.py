'''
Write a Python program to check car loan eligibility:
Salary >= 50,000 and Credit Score >= 700: "Eligible"
Otherwise: "Not Eligible"
'''

salary = int(input("Enter salary"))
creditScore=int(input("Enter credit score"))
if(salary>=50000 and creditScore>=700):
    print("Eligible")
else:
    print("Not eligible")