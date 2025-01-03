#Write a for loop statement to print the following series: 
#105 98 -------7

i=112
while i in range(112,0,-7):
    i-=7
    if i < 7:
        break
    print(i)