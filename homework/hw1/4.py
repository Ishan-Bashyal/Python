'''A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.'''

a = int(input("Enter marks: "))
if(a<25):
	print("F")
elif(a>=25 and a<45):
	print("E")
elif(a>=45 and a<50):
	print("D")
elif(a>=50 and a<60):
	print("C")
elif(a>=60 and a<80):
	print("B")
elif(a>=80):
	print("A")

