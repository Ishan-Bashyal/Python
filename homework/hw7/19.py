#Print multiplication table of  1,2,3,4,5,6,7,8 

i=0

while i<8:
    i+=1
    j=0
    while j<10:
        j+=1
        print(f'{i}X{j}={i*j}')
    print("\n")