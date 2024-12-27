#write a program to display integer from of a list. given list=[1,"a","c",2,3,4]

mylist=[1,"a","c",2,3,4]
for i in mylist:
    i=str(i)
    if(i.isnumeric()):
        print(i)
