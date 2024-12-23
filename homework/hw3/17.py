'''
Accept a color from the user:
If the color is "Red", print "Stop".
If "Yellow", print "Slow Down".
If "Green", print "Go".
Otherwise, print "Invalid Signal".
'''

color = input("Enter a color: ").capitalize()

if color == "Red":
    print("Stop")
elif color == "Yellow":
    print("Slow Down")
elif color == "Green":
    print("Go")
else:
    print("Invalid Signal")