'''
Ask the user if they want vegetarian or non-vegetarian. Based on the choice, give them options. 
If vegetarian, ask if they want "Salad" or "Pasta". 
If non-vegetarian, ask if they want "Chicken" or "Fish".
'''

choice = input("Do you want Vegetarian or Non-Vegetarian? ").lower()

if choice == "vegetarian":
    dish = input("Do you want Salad or Pasta? ").lower()
    print(f"You chose {dish}.")
elif choice == "non-vegetarian":
    dish = input("Do you want Chicken or Fish? ").lower()
    print(f"You chose {dish}.")
else:
    print("Invalid choice.")