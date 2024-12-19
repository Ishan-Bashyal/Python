'''
Create a Python program that greets the user with the message "Welcome to
the Pirate Island". Then, ask the user whether they want to go "left" or "right".
If they choose "right", print "Game Over". If they choose "left", ask if they want
to "dig for treasure" or "sail the ship". If they choose "dig for treasure", print
"Game Over". If they choose "sail the ship", ask them to choose between
"shark", "pirate ship", or "mermaid". If they choose "shark" or "pirate ship",
print "Game Over". If they choose "mermaid", print "You Win".
'''

print("Welcome to the Pirate Island")
user_choice = input("Do you want to go 'left' or 'right': ").lower()

if user_choice == "right":
    print("Game Over!")
elif user_choice == "left":
    user_choice = input("Do you want to 'dig for treasure' or 'sail the ship': ").lower()
    if user_choice == "dig for treasure":
        print("Game Over!")
    elif user_choice == "sail the ship":
        user_choice = input("Choose between 'shark', 'pirate ship', or 'mermaid': ").lower()
        if user_choice == "shark" or user_choice == "pirate ship":
            print("Game Over!")
        elif user_choice == "mermaid":
            print("You Win!")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")
