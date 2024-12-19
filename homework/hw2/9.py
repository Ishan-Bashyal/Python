#Accept the age of 4 people and display the oldest one

first = int(input("Enter age of First Person: "))
second = int(input("Enter age of Second Person: "))
third = int(input("Enter age of Third Person: "))
fourth = int(input("Enter age of Fourth Person: "))

if first >= second and first >= third and first >= fourth:
    print("First person is the oldest")
elif second >= third and second >= fourth and second >= first:
    print("Second person is the oldest")
elif third >= second and third >= first and third >= fourth:
    print("Third person is the oldest")
else:
    print("Fourth is the oldest")