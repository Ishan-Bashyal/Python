#You have two lists of numbers, and you need to find out which numbers appear in both lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
i = 0

while i < len(list1):
    if list1[i] in list2:
        print(f"Number {list1[i]} appears in both lists")
    i += 1
