#Write a for loop that removes all vowels (a, e, i, o, u) from a string.

vowels=['a','e','i','o','u']
str="notaaeiou"
for i in str:
    if(i not in vowels):
        print(i,end="")