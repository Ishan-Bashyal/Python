'''
Write a program starting with "Welcome to the Forest Adventure".
Prompt the user to choose a path: "left" or "right".
If "left", ask them to pick between "explore" or "rest".
    If "explore", print "You found treasure!".
    If "rest", print "You were attacked by wild animals. Game Over."
If "right", print "You fell into a trap. Game Over."
'''

print("Welcome to the Forest Adventure!")
path = input("Choose a path: 'left' or 'right': ").lower()

if path == "left":
    action = input("Do you want to 'explore' or 'rest'? ").lower()
    if action == "explore":
        print("You found treasure!")
    elif action == "rest":
        print("You were attacked by wild animals. Game Over.")
    else:
        print("Invalid choice.")
elif path == "right":
    print("You fell into a trap. Game Over.")
else:
    print("Invalid choice.")
