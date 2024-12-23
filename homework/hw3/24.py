'''
Accept the age, gender ('M', 'F'), and experience (years) and assign a role:
Age >= 21 and <= 35:
    Male:
        Experience >= 5: "Senior Developer"
        Experience < 5: "Junior Developer"
    Female:
        Experience >= 5: "Senior Analyst"
        Experience < 5: "Junior Analyst"
Age > 35:
    Male or Female: "Manager Role"
'''

age = int(input("Enter your age: "))
gender = input("Enter your gender ('M' for Male, 'F' for Female): ").upper()
experience = int(input("Enter your years of experience: "))

if 21 <= age <= 35:
    if gender == 'M':
        if experience >= 5:
            print("Senior Developer")
        else:
            print("Junior Developer")
    elif gender == 'F':
        if experience >= 5:
            print("Senior Analyst")
        else:
            print("Junior Analyst")
    else:
        print("Invalid gender input.")
elif age > 35:
    print("Manager Role")
else:
    print("Age not eligible for role assignment.")