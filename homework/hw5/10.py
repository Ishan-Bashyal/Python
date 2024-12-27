#Given list is lst=[1,2,3,4] but print 1 2 and 4 only 

list=[1,2,3,4]
for i in list:
    if(i==1 or i==2 or i==4):
        print(i,end=" ")