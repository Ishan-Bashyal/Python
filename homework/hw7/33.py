#Write a for loop which appends the type of each element in the first list to the second list.

first=['a','b',1,2,1.4,[1,2],(1,),'\n']
second=[]
i=0

while i < len(first):
    second.append(type(first[i]))
    i+=1

print(second)