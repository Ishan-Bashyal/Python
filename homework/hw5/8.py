#given list is [1,2,3,4] but expected output in new list [2,3,4,5]

list=[1,2,3,4]
newlist=[]
for i in list:
    newlist.append(i+1)
print("Newlist=",newlist)