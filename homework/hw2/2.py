'''
Create a Python program that starts by greeting the user with a message
"Welcome to Treasure Land". Then, prompt the user to choose a direction,
either "left" or "right". If the user chooses "right", print "Game Over". If the user
chooses "left", ask whether they want to "swim" or "wait". If they choose
"swim", print "Game Over". If they choose to "wait", ask them to select a color:
"red", "blue", or "yellow". If the user picks "blue" or "red", print "Game Over". If
they select "yellow", print "You Win".
'''

print('Welcome To Treasure Land')
direction=input("Choose a direction: (left) or (right): ")
if(direction!='right' and direction!='left'):
    print("Invalid choice")
else:
    if(direction=='right'):
        print("Game over")
    else:
        if(direction=='left'):
            choice=input("Do you want to: (swim) or (stay): ")
            if(choice!='swim'and choice!='stay'):
                print("Invalid choice")
            else:
                if(choice=='swim'):
                    print("Game over")
                else:
                    color=input("Enter a color: (red),(blue),(yellow)")
                    if(color!='red' and color!='blue' and color!='yellow'):
                        print("Invalid choice")
                    else:
                        if(color=='yellow'):
                            print('YOU WIN')
                        else:
                            print('Game over')

            