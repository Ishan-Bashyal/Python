'''
Accept string from the user and display only those characters which are 
present at an odd index.
'''

word = input("Enter a word: ")
for i in range(len(word)):
    if i % 2 != 0:
        print(f'{word[i]}')