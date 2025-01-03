#Python program that accepts a string and calculate the number of digits and letters and space

str=input("Write something: ")
digit=0
char=0
space=0
i=0

while i < len(str):
    typestr=str[i]
    if(typestr.isdigit()):
        digit+=1
    elif(typestr.isalpha()):
        char+=1
    else:
        space+=1
    i+=1
    
print("Total digits:",digit)
print("Total alphabets:",char)
print("Total spaces:",space)