#given list is [1,2,3,4] but expected output in new list [2,3,4,5]

list=[1,2,3,4]
newlist=[]
i=0
while i < len(list):
    newlist.append(i+2)
    i+=1
print("Newlist=",newlist)