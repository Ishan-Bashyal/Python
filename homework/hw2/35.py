'''
Create a Python program that greets the user with the message "Welcome to
the Magic Forest". Then, ask the user whether they want to go "north" or
"south". If they choose "south", print "Game Over". If they choose "north", ask
if they want to "cross the river" or "follow the path". If they choose "cross the
river", print "Game Over". If they choose "follow the path", ask them to choose
between "fairy", "ogre", or "elf". If they choose "ogre" or "fairy", print "Game
Over". If they choose "elf", print "You Win".
'''


print("Welcome to the Magic Forest")
user_choice = input("Do you want to go 'north' or 'south': ").lower()

if user_choice == "south":
    print("Game Over!")
elif user_choice == "north":
    user_choice = input("Do you want to 'cross the river' or 'follow the path': ").lower()
    if user_choice == "cross the river":
        print("Game Over!")
    elif user_choice == "follow the path":
        user_choice = input("Choose between 'fairy', 'ogre', or 'elf': ").lower()
        if user_choice == "ogre" or user_choice == "fairy":
            print("Game Over!")
        elif user_choice == "elf":
            print("You Win!")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")

