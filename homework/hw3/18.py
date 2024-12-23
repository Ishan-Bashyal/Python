'''
Accept temperature in Celsius from the user:
If greater than 40, print "Hot".
If between 20 and 39, print "Warm".
If less than 20, print "Cold".
'''

temperature = float(input("Enter temperature in Celsius: "))

if temperature > 40:
    print("Hot")
elif 20 <= temperature <= 39:
    print("Warm")
else:
    print("Cold")