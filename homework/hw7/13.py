#Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types

list=[1,2,3,'d',4,5,'a']
intlist=[]
strlist=[]
i=0

while i < len(list):
    newlist=list[i]
    i+=1
    if(isinstance(newlist,int)):
        intlist.append(newlist)
    elif(isinstance(newlist,str)):
        strlist.append(newlist)

print('Integer list:',intlist)
print('String list:',strlist)