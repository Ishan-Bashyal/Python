#Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.

given_list = [1, 2, 3, 4, "a", "b"]
int_list = []
str_list = []
i=0

while i < len(given_list):
    newlist=given_list[i]
    if isinstance(newlist, int):
        int_list.append(type(newlist))
    elif isinstance(newlist, str):
        str_list.append(type(newlist))
    i+=1

print("Integer types:", int_list)
print("String types:", str_list)
