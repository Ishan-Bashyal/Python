#Python program to count the space of a given string

str=input("Write something: ")
space=0
i=0

while i < len(str):
    spacelen=str[i]
    i+=1
    if(spacelen.isspace()):
        space+=1
print("Total spaces:",space)