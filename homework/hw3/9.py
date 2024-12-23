'''
Create a game with the message: "Welcome to the Space Adventure".
Ask the user to choose "land on Mars" or "fly to Jupiter".
If "land on Mars", ask if they want to "explore" or "build a base".
    If "explore", print "You found alien artifacts. You Win!"
    If "build a base", print "You ran out of resources. Game Over."
If "fly to Jupiter", print "Your spaceship crashed. Game Over."
'''

print("Welcome to the Space Adventure!")
choice = input("Do you want to 'land on Mars' or 'fly to Jupiter'? ").lower()

if choice == "Land on mars":
    action = input("Do you want to 'explore' or 'build a base'? ").lower()
    if action == "explore":
        print("You found alien artifacts. You Win!")
    elif action == "build a base":
        print("You ran out of resources. Game Over.")
    else:
        print("Invalid choice.")
elif choice == "fly to jupiter":
    print("Your spaceship crashed. Game Over.")
else:
    print("Invalid choice.")