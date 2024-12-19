'''
Create a Python program that greets the user with the message "Welcome to
the Space Mission". Then, ask the user whether they want to go "to the moon"
or "to Mars". If they choose "to Mars", print "Game Over". If they choose "to
the moon", ask if they want to "land on the surface" or "stay in orbit". If they
choose "land on the surface", print "Game Over". If they choose "stay in orbit",
ask them to choose between "alien", "asteroid", or "satellite". If they choose
"alien" or "asteroid", print "Game Over". If they choose "satellite", print "You
Win".
'''

print("Welcome to the Space Mission")
user_choice = input("Do you want to go 'to the moon' or 'to Mars': ").lower()

if user_choice == "to mars":
    print("Game Over!")
elif user_choice == "to the moon":
    user_choice = input("Do you want to 'land on the surface' or 'stay in orbit': ").lower()
    if user_choice == "land on the surface":
        print("Game Over!")
    elif user_choice == "stay in orbit":
        user_choice = input("Choose between 'alien', 'asteroid', or 'satellite': ").lower()
        if user_choice == "alien" or user_choice == "asteroid":
            print("Game Over!")
        elif user_choice == "satellite":
            print("You Win!")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")

