'''
Write a Python program to select players based on height:
Height >= 6 feet: Selected
Height < 6 feet: Not Selected
'''

height = float(input("Enter height in feet"))
if(height >= 6):
    print("Selected")
else:
    print("Not Selected")