#Write a for loop which appends the square of each number to the new list.

num = [1,2,3]
sq = []
i=0
while i < len(num):
    sq.append(num[i]*num[i])
    i+=1
print(sq)