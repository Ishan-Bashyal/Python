'''
Accept the grades from the user and display the grade according to the
following criteria:
Below 25 --D
25 to 45 -- C
45 to 50 -- B
50 to 60 --B+
60 to 80 -- A
Above 80 -- A+
'''

mark = int(input("Enter your Mark(0-100): "))
if mark < 25 and mark >= 0:
    grade = 'D'
elif mark < 45:
    grade = 'C'
elif mark < 50:
    grade = 'B'
elif mark < 60:
    grade = 'B+'
elif mark < 80:
    grade = 'A'
elif mark <= 100:
    grade = 'A+'


print(f"Your grade is: {grade}")