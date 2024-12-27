#given list is [1,2,3,4] but expected output is [1,8,27,64]

list=[1,2,3,4]
output=[]
for i in list:
    output.append(i**3)

print(output)