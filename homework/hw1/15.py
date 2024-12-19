'''
Write a Python program to give advice based on the temperature:
Temperature > 30°C: "It's hot, stay hydrated!"
Temperature between 15-30°C: "Enjoy the weather!"
Temperature < 15°C: "It's cold, wear warm clothes!"
'''
temp = int(input("Enter temperature in degree C"))
if(temp > 30):
    print("It's hot,stay hydrated")
elif(15 < temp < 30):
    print("Enjoy the weather!")
elif( temp < 15):
    print("It's cold,wear warm clothers!")
