#Given list is lst=[1,2,3,4] but print 1 and 2 only

list = [1,2,3,4]
i=-1
while i < len(list):
    i+=1
    if list[i] == 3:
        break
    print(list[i])