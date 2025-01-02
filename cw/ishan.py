for row in range(7):
    for column in range(5):
        if column==5 or (row==0 or row==6):
            print('*',end=" ")
        elif column==2 or row==7:
            print('*',end=" ")
        elif column==5 or row==0:
            print('*',end=" ")
        else:
            print(end="  ")
    print()

print('\n')

for row in range(7):
    for column in range(4):
        if (column==1 or column==2) and (row==0 or row==3 or row==6):
            print('*',end=" ")
        elif (column==0) and (row==1 or row==2):
            print('*',end=" ")
        elif (column==3) and (row==4 or row==5):
            print('*',end=" ")
        else:
            print(end="  ")
    print()

print('\n')


for row in range(7):
    for column in range(4):
        if column==0 or column==3:
            print('*',end=" ")
        elif row==3:
            print('*',end=" ")
        else:
            print(end="  ")
    print()

print('\n')


for row in range(6):
    for column in range(5):
        if (column==0 or column==4) and row!=0:
            print('*',end=" ")
        elif (column==1 or column==2 or column==3) and (row==0 or row==3):
            print('*',end=" ")
        else:
            print(end="  ")
    print()

print('\n')


for row in range(6):
    for column in range(6):
        if column==0 or column==5:
            print('*',end=" ")
        elif column==1 and row==1:
            print('*',end=" ")
        elif column==2 and row==2:
            print('*',end=" ")
        elif column==3 and row==3:
            print('*',end=" ")
        elif column==4 and row==4:
            print('*',end=" ")
        else:
            print(end="  ")
    print()
    

