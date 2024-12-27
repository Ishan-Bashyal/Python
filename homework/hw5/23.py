#Python program to count the space of a given string

str=input("Write something: ")
space=0

for i in str:
    if(i.isspace()):
        space+=1
print("Total spaces:",space)