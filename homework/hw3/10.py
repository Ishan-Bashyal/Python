'''
Start with "Welcome to the Haunted Castle".
Ask the user to choose "enter the castle" or "run away".
If "enter the castle", ask them to choose a door: "red", "green", or "black".
    If "red", print "You entered a room full of flames. Game Over."
    If "green", print "You found the treasure. You Win!"
    If "black", print "You were captured by ghosts. Game Over."
If "run away", print "You escaped safely."
'''

print("Welcome to the Haunted Castle!")
decision = input("Do you want to 'enter the castle' or 'run away'? ").lower()

if decision == "Enter the castle":
    door = input("Choose a door: 'red', 'green', or 'black': ").lower()
    if door == "red":
        print("You entered a room full of flames. Game Over.")
    elif door == "green":
        print("You found the treasure. You Win!")
    elif door == "black":
        print("You were captured by ghosts. Game Over.")
    else:
        print("Invalid choice.")
elif decision == "run away":
    print("You escaped safely.")
else:
    print("Invalid choice.")