#Given list is [1,2,3,4] but expected output is [1,"a",2,4]

list=[1,2,3,4]
newlist=[]

for i in list:
    if(i==2 or i==3):
        if(i==2):
            newlist.append('a')
        else:
            newlist.append(2)
    else:
        newlist.append(i)

print(newlist)