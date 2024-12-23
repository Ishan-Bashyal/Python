'''
Accept the price of an item from the user:
If the price is greater than 1000, apply a 20% discount and print the new price.
If between 500 and 1000, apply a 10% discount.
If less than 500, no discount.
'''

price = float(input("Enter the price of the item: "))

if price > 1000:
    discount = price * 0.20
    final_price = price - discount
    print("Discounted Price:", final_price)
elif 500 <= price <= 1000:
    discount = price * 0.10
    final_price = price - discount
    print("Discounted Price:", final_price)
else:
    print("No Discount. Final Price:", price)