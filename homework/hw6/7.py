'''
Write a Python program that simulates a login system. The program 
should prompt the user to enter a username and password. If both are 
correct (e.g., username is "admin" and password is "1234"), 
print "Login successful" and exit. If either is incorrect, 
print "Invalid credentials, try again." Allow the user up to 
3 attempts before locking them out with the message "Too many failed attempts."
'''

username='admin'
password='1234'
max_attempts=3
attempts=0

while attempts < max_attempts:
    username1= input("Enter your username: ")
    password1= input("Enter your password: ")
    if(
        username!= username1
        or password!= password1
        or username1 ==""
        or password ==""
    ):
        attempts+=1
        print('Invalid credentials, try again.')

    else:
        print("Login successful")
        break
else:
    print("Too many failed attempts.")