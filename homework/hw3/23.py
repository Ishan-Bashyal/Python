'''
Accept the age, gender ('M', 'F'), and academic score (out of 100) and determine eligibility:
Age >= 18 and <= 25:
    Male:
        Score >= 85: "Full Scholarship"
        Score >= 70: "Partial Scholarship"
        Score < 70: "No Scholarship"
    Female:
        Score >= 80: "Full Scholarship"
        Score >= 65: "Partial Scholarship"
        Score < 65: "No Scholarship"
'''

age = int(input("Enter your age: "))
gender = input("Enter your gender ('M' for Male, 'F' for Female): ").upper()
score = int(input("Enter your academic score (out of 100): "))

if 18 <= age <= 25:
    if gender == 'M':
        if score >= 85:
            print("Full Scholarship")
        elif score >= 70:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    elif gender == 'F':
        if score >= 80:
            print("Full Scholarship")
        elif score >= 65:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    else:
        print("Invalid gender input.")
else:
    print("Age not eligible for scholarship.")