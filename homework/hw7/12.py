#Given list is [1,2,3,4,5] separate the elements into odd and even categories.

list=[1,2,3,4,5]
evenlist=[]
oddlist=[]
i=0

while i < len(list):
    i+=1
    if(i%2==0):
        evenlist.append(i)
    else:
        oddlist.append(i)

print('Even list is',evenlist)
print('Odd list is',oddlist)