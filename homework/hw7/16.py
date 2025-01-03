#Python program to check the validity of username and password input by users


username='admin1234'
password='admin1234'
max_attempts=3
attempts=0

while attempts < max_attempts:
    username1= input("Enter your username: ")
    password1= input("Enter your password: ")
    if(
        username!= username1
        or password!= password1
        or len(password1)<8
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



    