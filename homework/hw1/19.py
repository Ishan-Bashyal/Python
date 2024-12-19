'''
Write a Python program to check login credentials:
Username: "admin", Password: "password123"
If correct, print "Access Granted"; otherwise, print "Access Denied."
'''

username = 'admin'
password = 'password123'
user = input("Enter username")
passw = input("Enter password")
if(username == user and password == passw):
    print("Accesss Granted")
else:
    print("Access Denied")