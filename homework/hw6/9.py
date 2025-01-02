'''
Write a Python program that prompts the user to enter a number. 
The program should determine whether the number is prime or not. 
If the number is prime, print "The number is prime." Otherwise, print
 "The number is not prime." Continue prompting the user until they enter "exit."
'''

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        break

    number = int(user_input)
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print("The number is not prime.")
                break
        else:
            print("The number is prime.")
    else:
        print("The number is not prime.")

