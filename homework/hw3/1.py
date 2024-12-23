'''
Take the price of an item as input. If the price is more than 1000, apply a 10% discount. 
Otherwise, check if the price is more than 500 and apply a 5% discount. Print the final price.
'''

price = float(input("Enter the price of the item: "))

if price > 1000:
    discount = price * 0.10
    final_price = price - discount
elif price > 500:
    discount = price * 0.05
    final_price = price - discount
else:
    final_price = price