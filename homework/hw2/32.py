'''
Create a program that suggests activities based on the weather:
 If the weather is sunny, recommend outdoor activities like hiking or a
picnic.
 If the weather is rainy, check if the user has a raincoat or umbrella:
 If yes, suggest going to a nearby mall or museum.
 If no, recommend staying home and watching movies.
'''

weather = input("Enter the weather (sunny/rainy/winter): ").lower()

if weather == "sunny":
    print("Hiking or a picnic will be great")
elif weather == "rainy":
    user_have = input("Do you have a raincoat or umbrella? (yes/no): ").lower()
    if user_have == "yes":
        print("Go to a mall or museum.")
    else:
        print("Stay home and watch movies.")
else:
    print("Invalid weather")
