'''
Write a Python program that prompts the user to repeatedly enter a name. 
If the user enters the phrase "good luck," the program keeps track of how many 
times the phrase has been entered. When the phrase has been entered three times, 
the program should display a message stating "You typed good luck three times." 
For each entry of "good luck" before the third occurrence, display the message 
"You typed the same word [count] times." Continue this process until the phrase 
has been entered three times.
'''

countermax=3
counter=0

while counter < countermax:
    userinput= input("Enter a name: ")
    if userinput=="good luck":
        counter+=1
        print(f"You typed the same word {counter} times.")
        if counter==countermax:
            print("You typed good luck three times.")
        continue

    else:
        print("Try again")
        continue
