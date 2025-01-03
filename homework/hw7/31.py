# 31. Write a for loop using an if statement, that appends each number to the new list if it's positive. 
# given lst1=[111, 32, -9, -45, -17, 9, 85, -10]

lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2=[]
i=0

while i < len(lst1):
    if(lst1[i]>0):
        lst2.append(lst1[i])
    i+=1
    
print(lst2)