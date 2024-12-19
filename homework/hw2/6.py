'''WAP which accepts marks of four subjects and display total marks,
percentage and
grade.
Hint: more than 70 –> distinction, more than 60 –> first, more than 40 –>
pass,
less than 40 –> fail'''


name = input("Enter your name: ")
science = int(input("Enter your marks in science: "))
math = int(input("Enter your marks in math: "))
social = int(input("Enter your marks in social: "))
computer = int(input("Enter your marks in computer: "))
total = science + math + social + computer
percent = (total / 400) * 100

if percent < 40:
    grade = 'fail'
elif percent < 60:
    grade = 'pass'
elif percent < 70:
    grade = 'first division'
else:
    grade = 'distinction'

print(f"\nTotal\t{total}\nPercent\t{percent}\nGrade\t{grade}")