#Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.

given_list = [1, 2, 3, 4, "a", "b"]
int_list = []
str_list = []

for i in given_list:
    if isinstance(i, int):
        int_list.append(type(i))
    elif isinstance(i, str):
        str_list.append(type(i))

print("Integer types:", int_list)
print("String types:", str_list)
