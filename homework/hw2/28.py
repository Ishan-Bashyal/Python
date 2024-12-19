'''
Ask the user for a subject score. If it's above 90, congratulate him. If it's
between 50 and 90, suggest improvement. Otherwise, advise on retaking the
course.
'''

score = int(input("Enter subject score: "))

if score > 90:
    print("Congratulations")
elif score >= 50 and score <= 90:
    print("Need improvement.")
else:
    print("Retake the course.")
