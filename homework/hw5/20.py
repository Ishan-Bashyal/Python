#Given list is lst=[1,2,3,4] but print 1 and 2 only

list = [1,2,3,4]
for i in list:
    if i == 3:
        break
    print(i)