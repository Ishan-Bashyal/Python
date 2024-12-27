#Given list is [1,2,3,4,5] separate the elements into odd and even categories.

list=[1,2,3,4,5]
evenlist=[]
oddlist=[]

for i in list:
    if(i%2==0):
        evenlist.append(i)
    else:
        oddlist.append(i)

print('Even list is',evenlist)
print('Odd list is',oddlist)