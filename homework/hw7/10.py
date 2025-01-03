#Given list is lst=[1,2,3,4] but print 1 2 and 4 only 

list=[1,2,3,4]
i=0
while i < len(list):
    i+=1
    if(i==1 or i==2 or i==4):
        print(i,end=" ")