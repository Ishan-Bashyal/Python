'''
A school decided to replace the desks in three classrooms. Each desk sits
two students. Given the number of students in each class, print the smallest
possible number of desks that can be purchased. The program should read
three integers: the number of students in each of the three
classes, a, b and c respectively.
Hint. In the first test there are three groups. The first group has 20 students
and thus needs 10 desks. The second group has 21 students, so they can
get by with no fewer than 11 desks. 11 desks are also enough for the third
group of 22 students. So, we need 32 desks in total.
'''

classa = int(input("Enter the no. of student in Class a: "))
classb = int(input("Enter the no. of student in Class b: "))
classc = int(input("Enter the no. of student in Class c: "))
if classa % 2 != 0:
    classa+=1
if classb % 2 != 0:
    classb+=1
if classc % 2 != 0:
    classc+=1
desk1 = classa // 2
desk2 = classb // 2
desk3 = classc // 2
print("Total Desk needed is: {}".format(desk1+desk2+desk3))


