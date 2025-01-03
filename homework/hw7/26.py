#Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). 
#Given range(50)

i=0
while i<=50:
    i+=1
    if(i<=7):
        print(i,end=" ")
    else:
        break