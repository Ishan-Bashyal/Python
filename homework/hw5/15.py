#Python program that accepts a string and calculate the number of digits and letters and space

str=input("Write something: ")
digit=0
char=0
space=0

for i in str:
    if(i.isdigit()):
        digit+=1
    elif(i.isalpha()):
        char+=1
    else:
        space+=1
    
print("Total digits:",digit)
print("Total alphabets:",char)
print("Total spaces:",space)