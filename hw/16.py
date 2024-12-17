'''
Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
Pizza: $10
Burger: $7
Pasta: $8
'''

menu = {'pizza': 10, 'burger': 7, 'pasta': 8}
option = input("Enter item name (Pizza, Burger, Pasta): ")
if option == 'pizza':
    print(f"The price of Pizza is {menu['pizza']}")
elif option == 'burger':
    print(f"The price of Burger is {menu['burger']}")
elif option == 'pasta':
    print(f"The price of Pasta is {menu['pasta']}")
else:
    print("Invalid Item")
