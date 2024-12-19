'''
Write a program to calculate the delivery cost based on the weight of the
package:
 If the package weighs less than 5kg, charge 5.
 If it weighs between 5kg and 20kg, charge 10.
 Check if the delivery is urgent; if yes, add $5 extra.
 If it weighs more than 20kg, charge 20.
'''


weight = float(input("Enter the weight of the package in kg: "))
urgent = input("Is the delivery urgent? (yes/no): ").lower()
delivery_cost = 0

if weight < 5:
    delivery_cost = 5
elif 5 <= weight <= 20:
    delivery_cost = 10
else:
    delivery_cost = 20

if urgent == 'yes':
    delivery_cost += 5

print("The total delivery cost is: $", delivery_cost)
