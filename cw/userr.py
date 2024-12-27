username='admin1234'
password='admin1234'

for i in range(3,0,-1):
    username1= input("Enter your username")
    password1= input("Enter your password")
    if(
        username!= username1
        or password!= password1
        or len(password1)<8
        or username1 ==""
        or password ==""
    ):
        if i==1:
            continue
        print(i-1,'Attempts left')
    else:
        print("Logged in successfully")
        break
else:
    print("You are blocked")