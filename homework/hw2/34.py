'''
Create a Python program that greets the user with the message "Welcome to
the Jungle Adventure". Then, ask the user whether they want to go "left" or
"right". If they choose "right", print "Game Over". If they choose "left", ask if
they want to "climb a tree" or "explore the cave". If they choose "climb a tree",
print "Game Over". If they choose "explore the cave", ask them to choose 
between "bear", "tiger", or "snake". If they choose "bear" or "tiger", print
"Game Over". If they choose "snake", print "You Win".
'''

print("Welcome to the Jungle Adventure")
user_choice = input("Do you want to go 'left' or 'right': ").lower()

if user_choice == "right":
    print("Game Over!")
elif user_choice == "left":
    user_choice = input("Do you want to 'climb a tree' or 'explore the cave': ").lower()
    if user_choice == "climb a tree":
        print("Game Over!")
    elif user_choice == "explore the cave":
        user_choice = input("Choose between 'bear', 'tiger', or 'snake': ").lower()
        if user_choice == "bear" or user_choice == "tiger":
            print("Game Over!")
        elif user_choice == "snake":
            print("You Win!")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")

