#You have two lists of numbers, and you need to find out which numbers appear in both lists.

list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
for i in list1:
    if(i in list2):
        print(f"Number {i} is appear in both lists")