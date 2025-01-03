#write a program to display integer from of a list. given list=[1,"a","c",2,3,4]

mylist = [1, "a", "c", 2, 3, 4]
i = 0

while i < len(mylist):
    item = mylist[i]
    if type(item) == int:
        print(item)
    i += 1
        
