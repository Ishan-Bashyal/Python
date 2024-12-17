#Write a Python program that takes a color as input ("Red", "Yellow", "Green") and outputs the corresponding action ("Stop", "Get Ready", "Go").

color = input("Enter color")
if(color == 'red'):
    print("Stop")
elif(color == 'yellow'):
    print("Get Ready")
elif(color == 'green'):
    print('Go')
else:
    print("Invalid input")