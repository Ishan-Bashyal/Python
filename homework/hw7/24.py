#given list is [1,2,3,4] but expected output is [1,8,27,64]

list=[1,2,3,4]
output=[]
i=0

while i < len(list):
    newlist=list[i]
    i+=1
    output.append(newlist**3)

print(output)