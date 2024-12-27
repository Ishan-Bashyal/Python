#Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types

list=[1,2,3,'d',4,5,'a']
intlist=[]
strlist=[]
for i in list:
    if(isinstance(i,int)):
        intlist.append(i)
    elif(isinstance(i,str)):
        strlist.append(i)

print('Integer list:',intlist)
print('String list:',strlist)